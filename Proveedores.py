from qtpy.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QMessageBox
from qtpy.QtCore import Qt
from conexion import DBConnection
from FormulariosProveedor import FormularioProveedor  # Asegúrate de tener un formulario adecuado para los proveedores


class ProveedoresView(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        
        # Título
        title_label = QLabel("Gestión de Proveedores")
        title_label.setStyleSheet("font: bold 16pt Arial; color: black;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Buscador
        search_layout = QHBoxLayout()
        search_label = QLabel("Buscar Proveedor:")
        search_label.setStyleSheet("font: 12pt Arial; color: black;")
        search_layout.addWidget(search_label)

        self.search_entry = QLineEdit()
        self.search_entry.setStyleSheet("""
            font: 12pt Arial;
            padding: 5px;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            color: black;
        """)
        search_layout.addWidget(self.search_entry)

        search_button = QPushButton("Buscar")
        search_button.setStyleSheet("""
            background-color: #3498db; 
            color: white; 
            font: 12pt Arial; 
            border-radius: 5px;
            padding: 8px;
        """)
        search_button.clicked.connect(self.search_provider)
        search_layout.addWidget(search_button)

        main_layout.addLayout(search_layout)

        # Tabla de proveedores
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Id", "Nombre", "Contacto"])
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                font: 12pt Arial;
                gridline-color: #bdc3c7;
                border: 1px solid #bdc3c7;
            }
            QTableWidget::item {
                padding: 10px;
                border: 1px solid #ecf0f1;
                color: black;
            }
            QTableWidget::item:selected {
                background-color: #a0d0f0;
            }
        """)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 200)
        main_layout.addWidget(self.table)

        # Botones
        button_layout = QHBoxLayout()

        create_button = QPushButton("Crear")
        create_button.setStyleSheet("""
            background-color: #2ecc71;
            color: white;
            font: 12pt Arial;
            border-radius: 5px;
            padding: 10px;
        """)
        create_button.clicked.connect(self.create_provider)
        button_layout.addWidget(create_button)

        modify_button = QPushButton("Modificar")
        modify_button.setStyleSheet("""
            background-color: #f39c12;
            color: white;
            font: 12pt Arial;
            border-radius: 5px;
            padding: 10px;
        """)
        modify_button.clicked.connect(self.modify_provider)
        button_layout.addWidget(modify_button)

        delete_button = QPushButton("Eliminar")
        delete_button.setStyleSheet("""
            background-color: #e74c3c;
            color: white;
            font: 12pt Arial;
            border-radius: 5px;
            padding: 10px;
        """)
        delete_button.clicked.connect(self.delete_provider)
        button_layout.addWidget(delete_button)

        main_layout.addLayout(button_layout)

        self.load_providers()

    def setup_ui(self):
        # Inicializa el QTableWidget
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)  # Suponiendo 3 columnas: ID, Nombre, Contacto
        self.table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Contacto"])
        
        # Crea el layout y agrega el QTableWidget
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        # Aquí puedes cargar los proveedores en la tabla
        self.load_providers()
        
        

    def load_providers(self):
        """Carga los proveedores desde la base de datos en la tabla"""
        db = DBConnection()
        db.connect()
        proveedores = db.fetch_proveedores()
        db.close()

        self.update_table(proveedores)

    def search_provider(self):
        """Función para buscar un proveedor basado en el texto del buscador"""
        search_text = self.search_entry.text().lower()
        db = DBConnection()
        db.connect()
        proveedores = db.fetch_proveedores()
        db.close()

        filtered_providers = [
            provider for provider in proveedores if search_text in str(provider[0]).lower() or
                                                   search_text in provider[1].lower()
        ]

        self.update_table(filtered_providers)

    def update_table(self, proveedores):
        """Actualiza la tabla con los proveedores filtrados o cargados"""
        self.table.setRowCount(len(proveedores))
        for row_num, provider in enumerate(proveedores):
            for col_num, value in enumerate(provider):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(Qt.black)  
                self.table.setItem(row_num, col_num, item)

    def create_provider(self):
        """Abre un formulario para crear un nuevo proveedor"""
        formulario = FormularioProveedor()
        if formulario.exec_():  # Muestra el formulario como una ventana modal
            name = formulario.name_input.text()
            contact = formulario.contact_input.text()

            # Crear el proveedor en la base de datos
            db = DBConnection()
            db.connect()
            db.create_provider(name, contact)  # Llama al método create_provider
            db.close()

            QMessageBox.information(self, "Crear Proveedor", "Proveedor creado exitosamente.")
            self.load_providers()  # Recarga los proveedores para mostrar el nuevo



    def modify_provider(self):
        """Abre un formulario para modificar un proveedor existente"""
        # Verifica si hay una fila seleccionada
        selected_row = self.table.selectedIndexes()  # Cambié aquí de table_widget a table
        if selected_row:
            # Suponiendo que la columna 0 tiene el ID del proveedor
            provider_id = self.table.item(selected_row[0].row(), 0).text()  # Cambié de table_widget a table
            name = self.table.item(selected_row[0].row(), 1).text()  # Cambié de table_widget a table
            contact = self.table.item(selected_row[0].row(), 2).text()  # Cambié de table_widget a table

            formulario = FormularioProveedor(name, contact)
            if formulario.exec_():  # Muestra el formulario como una ventana modal
                new_name = formulario.name_input.text()
                new_contact = formulario.contact_input.text()

                # Actualiza el proveedor en la base de datos
                db = DBConnection()
                db.connect()
                db.update_provider(provider_id, new_name, new_contact)
                db.close()

                QMessageBox.information(self, "Modificar Proveedor", "Proveedor modificado exitosamente.")
                self.load_providers()  # Recarga los proveedores para mostrar los cambios
        else:
            QMessageBox.warning(self, "Selección inválida", "Por favor, selecciona un proveedor para modificar.")


    def delete_provider(self):
        """Elimina el proveedor seleccionado de la base de datos"""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Eliminar Proveedor", "Por favor, selecciona un proveedor para eliminar.")
            return

        confirm = QMessageBox.question(
            self,
            "Eliminar Proveedor",
            "¿Estás seguro de que deseas eliminar este proveedor?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.No:
            return

        provider_id = self.table.item(selected_row, 0).text()

        db = DBConnection()
        db.connect()
        db.delete_provider(provider_id)
        db.close()

        QMessageBox.information(self, "Eliminar Proveedor", "Proveedor eliminado exitosamente.")
        self.load_providers()  # Recarga la lista de proveedores

