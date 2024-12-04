from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QScrollArea, QStackedWidget
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import os
import sys
import shutil
import mysql.connector
from mysql.connector import Error

class TiendaView(QWidget):
    def __init__(self, is_user=True):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Estilos generales
        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
            border-radius: 10px;
        """)

        # Ruta de la raíz del proyecto
        self.project_root = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Crear carpeta para guardar imágenes
        self.image_folder = os.path.join(self.project_root, "img")
        os.makedirs(self.image_folder, exist_ok=True)

        # Conectar a la base de datos MySQL
        self.db_connection = self.connect_to_db()
        self.cursor = self.db_connection.cursor()

        # Encabezado
        product_header = QLabel("Catálogo de Productos")
        product_header.setFont(QFont("Arial", 16, QFont.Bold))
        product_header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(product_header)

        # Crear área de desplazamiento (scroll area)
        scroll_area = QScrollArea()
        self.layout.addWidget(scroll_area)

        # Contenedor de productos
        self.product_container = QWidget()
        self.product_layout = QGridLayout()  # Cambiar a QGridLayout para la cuadrícula
        self.product_container.setLayout(self.product_layout)
        
        # Configurar el scroll area
        scroll_area.setWidget(self.product_container)
        scroll_area.setWidgetResizable(True)

        # Cargar productos desde la base de datos
        self.products = self.load_data()

        # Agregar los productos a la cuadrícula
        for index, product in enumerate(self.products):
            self.add_product_to_grid(product, index)

        # Botón para actualizar la lista de productos
        update_button = QPushButton("Actualizar")
        update_button.setStyleSheet("""
            background-color: orange; 
            color: white; 
            font-size: 14px; 
            padding: 8px; 
            border-radius: 5px;
        """)
        update_button.clicked.connect(self.actualizar_productos)
        self.layout.addWidget(update_button)

    def connect_to_db(self):
        """Conectar a la base de datos MySQL."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Cambia esto según tu configuración
                password="",  # Cambia esto según tu configuración
                database="Tienda"  # Nombre de la base de datos MySQL
            )
            if connection.is_connected():
                print("Conexión exitosa a la base de datos MySQL.")
            return connection
        except Error as e:
            print(f"Error de conexión a MySQL: {e}")
            sys.exit(1)

    def add_product_to_grid(self, product, index):
        """Agrega un producto a la cuadrícula."""
        row = index // 3  # Determina la fila
        col = index % 3   # Determina la columna
        product_widget = self.create_product_widget(
            product[1], product[2], product[3], product[5]
        )
        self.product_layout.addWidget(product_widget, row, col)


    def create_product_widget(self, name, price, image_path=None, provider_id=None):
        """Crea un widget de producto con su información."""
        product_widget = QWidget()
        product_layout = QVBoxLayout()
        product_widget.setLayout(product_layout)

        # Estilo para separar cada producto
        product_widget.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            margin: 10px;
        """)

        # Imagen
        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("""
            background-color: lightblue; 
            border: 1px solid black; 
            border-radius: 5px;
        """)
        image_label.setFixedSize(150, 100)
        
        if image_path and os.path.exists(image_path):
            try:
                pixmap = QPixmap(image_path).scaled(150, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label.setPixmap(pixmap)
            except Exception as e:
                image_label.setText(f"Error: {str(e)}")
        else:
            image_label.setText("No Image")
        
        product_layout.addWidget(image_label)

        # Nombre del producto
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        """)
        product_layout.addWidget(name_label)

        # Proveedor (Id_Proveedor)
        provider_label = QLabel(f"Proveedor: {provider_id}")
        provider_label.setAlignment(Qt.AlignCenter)
        provider_label.setStyleSheet("""
            font-size: 12px;
            color: #7f8c8d;
        """)
        product_layout.addWidget(provider_label)

        # Precio
        price_label = QLabel(f"$ {price:.2f}")
        price_label.setAlignment(Qt.AlignCenter)
        price_label.setFont(QFont("Arial", 12, QFont.Bold))
        price_label.setStyleSheet("""
            font-size: 14px;
            color: #27ae60;
        """)
        product_layout.addWidget(price_label)

        # Botón para agregar al carrito debajo del producto
        add_to_cart_button = QPushButton("Agregar al Carrito")
        add_to_cart_button.setStyleSheet("""
            background-color: green; 
            color: white; 
            font-size: 14px; 
            padding: 8px; 
            border-radius: 5px;
            border: 1px solid #27ae60;
            margin-top: 10px;
        """)
        add_to_cart_button.clicked.connect(lambda: self.agregar_al_carrito(name))
        product_layout.addWidget(add_to_cart_button)

        return product_widget

    def agregar_al_carrito(self, product_name):
        """Simula agregar un producto al carrito."""
        QMessageBox.information(self, "Carrito", f"Producto '{product_name}' agregado al carrito.")

    def actualizar_productos(self):
        """Función para actualizar la lista de productos."""
        self.products = self.load_data()

        # Limpiar la cuadrícula actual
        for i in reversed(range(self.product_layout.count())):
            widget = self.product_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Agregar los productos actualizados a la cuadrícula
        for index, product in enumerate(self.products):
            self.add_product_to_grid(product, index)
    def load_data(self):
        """Carga los productos desde la base de datos."""
        self.cursor.execute("SELECT p.Id_Producto, p.Nombre, p.Precio, p.Imagen, p.Id_Proveedor, pr.Nombre as Proveedor FROM Productos p JOIN Proveedores pr ON p.Id_Proveedor = pr.Id_Proveedor")
        return self.cursor.fetchall()
  
