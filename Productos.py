from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QScrollArea
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import os
import sys
import shutil
import mysql.connector
from mysql.connector import Error

class ProductosView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Ruta de la raíz del proyecto
        self.project_root = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Crear carpeta para guardar imágenes
        self.image_folder = os.path.join(self.project_root, "img")
        os.makedirs(self.image_folder, exist_ok=True)

        # Conectar a la base de datos MySQL
        self.db_connection = self.connect_to_db()
        self.cursor = self.db_connection.cursor()

        # Estilo general de la vista
        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
            border-radius: 10px;
        """)

        # Encabezado
        product_header = QLabel("Gestíon de Productos")
        product_header.setFont(QFont("Arial", 16, QFont.Bold))
        product_header.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(product_header)

        # Crear área de desplazamiento (scroll area)
        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: 1px solid #bdc3c7; border-radius: 10px;")  # Bordes del área de desplazamiento
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

        # Botón para crear un nuevo producto
        create_product_button = QPushButton("Crear Producto")
        create_product_button.setStyleSheet("""
            background-color: blue; 
            color: white; 
            font-size: 14px; 
            padding: 8px; 
            border-radius: 5px;
        """)
        create_product_button.clicked.connect(self.crear_producto)
        self.layout.addWidget(create_product_button)

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
        product_widget.setStyleSheet("""
            background-color: #ffffff;
            border: 1px solid #bdc3c7;
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
        """)

        # Imagen
        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("background-color: lightblue; border: 1px solid black;")
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

        # Botón para editar imagen
        edit_image_button = QPushButton("Editar Imagen")
        edit_image_button.setStyleSheet("""
            background-color: #3498db; 
            color: white; 
            font-size: 12px; 
            border-radius: 5px; 
            padding: 5px;
        """)
        edit_image_button.clicked.connect(lambda: self.editar_imagen(image_label, name))
        product_layout.addWidget(edit_image_button)

        # Nombre del producto
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignCenter)
        product_layout.addWidget(name_label)

        # Proveedor (Id_Proveedor)
        provider_label = QLabel(f"Proveedor: {provider_id}")
        provider_label.setAlignment(Qt.AlignCenter)
        product_layout.addWidget(provider_label)

        # Precio
        price_label = QLabel(f"$ {price:.2f}")
        price_label.setAlignment(Qt.AlignCenter)
        price_label.setFont(QFont("Arial", 12, QFont.Bold))
        product_layout.addWidget(price_label)

        # Botón para eliminar producto
        delete_button = QPushButton("Eliminar Producto")
        delete_button.setStyleSheet("""
            background-color: #e74c3c;
            color: white;
            font-size: 12px;
            border-radius: 5px;
            padding: 5px;
        """)
        delete_button.clicked.connect(lambda: self.eliminar_producto(product_widget, name))
        product_layout.addWidget(delete_button)

        return product_widget

    def editar_imagen(self, image_label, product_name):
        """Permite al usuario seleccionar una imagen y cargarla en el widget."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Imagen", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options
        )
        if file_path:
            try:
                # Copiar la imagen seleccionada al directorio 'img'
                file_name = f"{product_name}_{os.path.basename(file_path)}"
                dest_path = os.path.join(self.image_folder, file_name)
                shutil.copy(file_path, dest_path)

                # Actualizar la etiqueta de imagen
                pixmap = QPixmap(dest_path).scaled(150, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label.setPixmap(pixmap)

                # Actualizar la base de datos con la nueva ruta de imagen
                self.cursor.execute("UPDATE Productos SET Imagen = %s WHERE Nombre = %s", (dest_path, product_name))
                self.db_connection.commit()

                QMessageBox.information(self, "Imagen Subida", f"Imagen guardada en: {dest_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar la imagen: {str(e)}")

    def eliminar_producto(self, product_widget, product_name):
        """Elimina un producto de la cuadrícula y de la base de datos."""
        product_widget.setParent(None)
        self.cursor.execute("DELETE FROM Productos WHERE Nombre = %s", (product_name,))
        self.db_connection.commit()

    def crear_producto(self):
        """Permite agregar un nuevo producto."""
        name, ok_name = QInputDialog.getText(self, "Nuevo Producto", "Ingrese el nombre del producto:")
        if not ok_name or not name.strip():
            return

        price, ok_price = QInputDialog.getDouble(self, "Nuevo Producto", "Ingrese el precio:", decimals=2)
        if not ok_price:
            return

        provider_id, ok_provider = QInputDialog.getInt(self, "Nuevo Producto", "Ingrese el ID del proveedor:")
        if not ok_provider:
            return

        # Asegurarse de que la imagen no sea None
        image_path = None  # Aquí se puede modificar para aceptar una imagen, si es necesario

        new_product = (name, price, image_path, provider_id)
        self.cursor.execute("INSERT INTO Productos (Nombre, Precio, Imagen, Id_Proveedor) VALUES (%s, %s, %s, %s)", new_product)
        self.db_connection.commit()

        # Recargar los productos
        self.products = self.load_data()
        self.add_product_to_grid(self.products[-1], len(self.products) - 1)

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

# class MainApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.tienda_view = TiendaView()
#         self.setCentralWidget(self.tienda_view)
#         self.setWindowTitle("Tienda")
#         self.setGeometry(100, 100, 800, 600)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainApp()
#     window.show()
#     sys.exit(app.exec_())