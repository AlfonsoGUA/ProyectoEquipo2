from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ProductosView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        header = QLabel("GESTIÓN DE PRODUCTOS")
        header.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        add_product_button = QPushButton("Agregar Producto")
        layout.addWidget(add_product_button)

        view_products_button = QPushButton("Ver Productos")
        layout.addWidget(view_products_button)
