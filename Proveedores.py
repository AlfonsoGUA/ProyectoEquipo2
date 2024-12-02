from qtpy.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QScrollArea
from qtpy.QtCore import Qt
from conexion import DBConnection  

class ProveedoresView(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        
        
        title_label = QLabel("Gestión de Proveedores")
        title_label.setStyleSheet("font: bold 16pt Arial; color: black;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

       
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
        search_button.clicked.connect(self.search_user)
        search_layout.addWidget(search_button)

        main_layout.addLayout(search_layout)

       
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

        
        self.load_providers()

    def load_providers(self):
        """Carga los proveedores desde la base de datos en la tabla"""
        db = DBConnection()
        db.connect()
        proveedores = db.fetch_proveedores()
        db.close()
        
        self.table.setRowCount(len(proveedores))
        for row_num, proveedor in enumerate(proveedores):
            for col_num, value in enumerate(proveedor):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(Qt.black)  
                self.table.setItem(row_num, col_num, item)

    def search_user(self):
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

    def create_user(self):
        """Placeholder para crear un proveedor"""
        print("Función de crear proveedor no implementada.")

    def modify_user(self):
        """Placeholder para modificar un proveedor"""
        print("Función de modificar proveedor no implementada.")

    def delete_user(self):
        """Placeholder para eliminar un proveedor"""
        print("Función de eliminar proveedor no implementada.")
