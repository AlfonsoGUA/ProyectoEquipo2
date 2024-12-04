from qtpy.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QDialog
from qtpy.QtCore import Qt
from conexion import DBConnection
from Formularios import FormularioUsuario


class UsuariosView(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)

        # Título
        title_label = QLabel("Gestión de Usuarios")
        title_label.setStyleSheet("font: bold 16pt Arial; color: black;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Buscador
        search_layout = QHBoxLayout()
        search_label = QLabel("Buscar Usuario:")
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
        search_button.clicked.connect(self.search_user)
        search_layout.addWidget(search_button)

        main_layout.addLayout(search_layout)

        # Tabla de usuarios
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Id", "Nombre", "Correo", "Contraseña", "Rol"])
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
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 100)
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
        create_button.clicked.connect(self.create_user)
        button_layout.addWidget(create_button)

        modify_button = QPushButton("Modificar")
        modify_button.setStyleSheet("""
            background-color: #f39c12;
            color: white;
            font: 12pt Arial;
            border-radius: 5px;
            padding: 10px;
        """)
        modify_button.clicked.connect(self.modify_user)
        button_layout.addWidget(modify_button)

        delete_button = QPushButton("Eliminar")
        delete_button.setStyleSheet("""
            background-color: #e74c3c;
            color: white;
            font: 12pt Arial;
            border-radius: 5px;
            padding: 10px;
        """)
        delete_button.clicked.connect(self.delete_user)
        button_layout.addWidget(delete_button)

        main_layout.addLayout(button_layout)

        self.load_users()

    def load_users(self):
        """Carga los usuarios desde la base de datos en la tabla"""
        db = DBConnection()
        db.connect()
        usuarios = db.fetch_usuarios()
        db.close()

        self.update_table(usuarios)

    def update_table(self, usuarios):
        """Actualiza la tabla con los usuarios filtrados o cargados"""
        self.table.setRowCount(len(usuarios))
        for row_num, usuario in enumerate(usuarios):
            for col_num, value in enumerate(usuario):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(Qt.black)
                self.table.setItem(row_num, col_num, item)

    def search_user(self):
        """Función para buscar un usuario basado en el texto del buscador"""
        search_text = self.search_entry.text().lower()
        db = DBConnection()
        db.connect()
        usuarios = db.fetch_usuarios()
        db.close()

        filtered_usuarios = [
            usuario for usuario in usuarios if search_text in str(usuario[0]).lower() or
                                                search_text in usuario[1].lower() or
                                                search_text in usuario[2].lower()
        ]

        self.update_table(filtered_usuarios)

    def create_user(self):
        """Abre un formulario para crear un nuevo usuario"""
        formulario = FormularioUsuario()
        if formulario.exec_():  # Muestra el formulario como una ventana modal
            QMessageBox.information(self, "Crear Usuario", "Usuario creado exitosamente.")
            self.load_users()  # Recarga los usuarios para mostrar el nuevo

    def modify_user(self):
        """Modifica los datos del usuario seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Modificar Usuario", "Por favor, selecciona un usuario para modificar.")
            return
        
        # Obtiene los datos del usuario seleccionado
        user_id = self.table.item(selected_row, 0).text()
        user_name = self.table.item(selected_row, 1).text()
        user_email = self.table.item(selected_row, 2).text()
        user_password = self.table.item(selected_row, 3).text()
        user_role = self.table.item(selected_row, 4).text()

        # Crea el formulario con los datos del usuario seleccionado
        formulario = FormularioUsuario(user_id, user_name, user_email, user_password, user_role)
        if formulario.exec_() == QDialog.Accepted:
            # Después de editar el usuario, guarda los cambios en la base de datos
            db = DBConnection()
            db.connect()

            # Cambia a acceso correcto de los valores del formulario
            db.modificar_usuario(user_id, 
                             formulario.nombre_input.text(),  # Aquí cambiamos user_name por nombre_input
                             formulario.correo_input.text(),
                             formulario.password_input.text(),
                             formulario.role_combo.currentText())

            db.close()
            self.load_users()  # Recarga los usuarios en la tabla

    def delete_user(self):
        """Elimina el usuario seleccionado de la base de datos."""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Eliminar Usuario", "Por favor, selecciona un usuario para eliminar.")
            return

        confirm = QMessageBox.question(
            self,
            "Eliminar Usuario",
            "¿Estás seguro de que deseas eliminar este usuario?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.No:
            return

        user_id = self.table.item(selected_row, 0).text()

        db = DBConnection()
        db.connect()
        db.delete_usuario(user_id)
        db.close()

        QMessageBox.information(self, "Eliminar Usuario", "Usuario eliminado exitosamente.")
        self.load_users()
