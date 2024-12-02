from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class ProveedoresView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        header = QLabel("GESTIÓN DE PROVEEDORES")
        header.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        add_supplier_button = QPushButton("Agregar Proveedor")
        layout.addWidget(add_supplier_button)

        view_suppliers_button = QPushButton("Ver Proveedores")
        layout.addWidget(view_suppliers_button)
