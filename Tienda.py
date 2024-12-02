from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class TiendaView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

    
        product_header = QLabel("PRODUCTOS")
        product_header.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        product_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(product_header)

        product_grid = QGridLayout()
        layout.addLayout(product_grid)

        for row in range(2): 
            for col in range(3):  
                
                product_widget = self.create_product_widget(f"Producto {row * 3 + col + 1}", "Proveedor", 306.99)
                product_grid.addWidget(product_widget, row, col)

    def create_product_widget(self, name, provider, price):
        """Crea un widget de producto con su información."""
        product_widget = QWidget()
        product_layout = QVBoxLayout()
        product_widget.setLayout(product_layout)

    
        image_label = QLabel("No Image")
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        image_label.setFixedSize(150, 100)
        product_layout.addWidget(image_label)

      
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        product_layout.addWidget(name_label)

       
        provider_label = QLabel(provider)
        provider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        product_layout.addWidget(provider_label)

     
        price_label = QLabel(f"$ {price:.2f}")
        price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        price_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        product_layout.addWidget(price_label)

        add_button = QPushButton("Agregar")
        add_button.setStyleSheet("color: green; font-weight: bold;")
        product_layout.addWidget(add_button)

        return product_widget
