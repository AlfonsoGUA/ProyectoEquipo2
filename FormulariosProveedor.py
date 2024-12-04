from qtpy.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton

class FormularioProveedor(QDialog):
    def __init__(self, provider_id=None, name=None, contact=None):
        super().__init__()

        self.setWindowTitle("Formulario Proveedor")
        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        """)

        # Atributos de proveedor
        self.provider_id = provider_id
        self.name_input = QLineEdit(name if name else "")
        self.contact_input = QLineEdit(contact if contact else "")

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Nombre
        name_layout = QHBoxLayout()
        name_label = QLabel("Nombre:")
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        main_layout.addLayout(name_layout)

        # Contacto
        contact_layout = QHBoxLayout()
        contact_label = QLabel("Contacto:")
        contact_layout.addWidget(contact_label)
        contact_layout.addWidget(self.contact_input)
        main_layout.addLayout(contact_layout)

        # Botones
        button_layout = QHBoxLayout()
        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancelar")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        main_layout.addLayout(button_layout)

    def accept(self):
        """Aceptar el formulario y pasar los datos al controlador"""
        if not self.name_input.text() or not self.contact_input.text():
            # Mostrar advertencia si no se ingresan datos
            QMessageBox.warning(self, "Campos vacíos", "Todos los campos deben ser completados.")
            return
        super().accept()
