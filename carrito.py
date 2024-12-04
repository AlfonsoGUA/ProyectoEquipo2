from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class CarritoView(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Título del carrito
        carrito_title = QLabel("Carrito de Compras")
        carrito_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(carrito_title)

        # Crear tabla para mostrar productos en el carrito
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Nombre, Precio, Cantidad, Acción
        self.table.setHorizontalHeaderLabels(["Producto", "Precio", "Cantidad", "Acción"])
        self.layout.addWidget(self.table)

        # Botón para realizar la compra
        buy_button = QPushButton("Realizar Compra")
        buy_button.setStyleSheet("""
            background-color: #2980b9; 
            color: white; 
            font: 14px Arial; 
            padding: 8px; 
            border-radius: 5px;
        """)
        buy_button.clicked.connect(self.realizar_compra)
        self.layout.addWidget(buy_button)

        # Lista de productos en el carrito
        self.cart_items = []

    def add_to_cart(self, product):
        """Agrega un producto al carrito."""
        self.cart_items.append(product)
        self.update_cart()

    def update_cart(self):
        """Actualiza la tabla del carrito con los productos."""
        self.table.setRowCount(len(self.cart_items))

        for row_num, product in enumerate(self.cart_items):
            self.table.setItem(row_num, 0, QTableWidgetItem(product["name"]))
            self.table.setItem(row_num, 1, QTableWidgetItem(str(product["price"])))
            self.table.setItem(row_num, 2, QTableWidgetItem("1"))  # Por defecto, la cantidad es 1

            # Botón para eliminar del carrito
            remove_button = QPushButton("Eliminar")
            remove_button.setStyleSheet("""
                background-color: #e74c3c; 
                color: white; 
                font: 12px Arial; 
                border-radius: 5px;
                padding: 5px;
            """)
            remove_button.clicked.connect(lambda row=row_num: self.remove_from_cart(row))  # Eliminar producto
            self.table.setCellWidget(row_num, 3, remove_button)

    def remove_from_cart(self, row):
        """Elimina un producto del carrito."""
        self.cart_items.pop(row)
        self.update_cart()

    def realizar_compra(self):
        """Simula la compra del carrito."""
        if not self.cart_items:
            QMessageBox.warning(self, "Carrito Vacío", "No hay productos en el carrito para comprar.")
        else:
            QMessageBox.information(self, "Compra Realizada", "Compra realizada con éxito.")
            self.cart_items.clear()  # Vaciar el carrito después de la compra
            self.update_cart()  # Actualizar la tabla
