from qtpy.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from conexion import DBConnection

class FormularioUsuario(QDialog):
    def __init__(self, user_id=None, user_name=None, user_email=None, user_password=None, user_role=None):
        super().__init__()

        self.setWindowTitle("Modificar Usuario")
        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Campos del formulario
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")
        self.nombre_input.setStyleSheet("""
            font: 12pt Arial;
            padding: 5px;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            color: black;
        """)
        if user_name:  # Si hay un nombre, lo pre-llena
            self.nombre_input.setText(user_name)
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.nombre_input)

        self.correo_input = QLineEdit()
        self.correo_input.setPlaceholderText("Correo")
        self.correo_input.setStyleSheet("""
            font: 12pt Arial;
            padding: 5px;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            color: black;
        """)
        if user_email:  # Si hay un correo, lo pre-llena
            self.correo_input.setText(user_email)
        layout.addWidget(QLabel("Correo:"))
        layout.addWidget(self.correo_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            font: 12pt Arial;
            padding: 5px;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            color: black;
        """)
        if user_password:  # Si hay una contraseña, lo pre-llena
            self.password_input.setText(user_password)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.password_input)

        # Selección de rol
        self.role_combo = QComboBox()
        self.role_combo.addItems(["admin", "usuario"])
        if user_role:  # Si hay un rol, lo pre-llena
            self.role_combo.setCurrentText(user_role)
        self.role_combo.setStyleSheet("""
            font: 12pt Arial;
            padding: 5px;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            color: black;
        """)
        layout.addWidget(QLabel("Rol:"))
        layout.addWidget(self.role_combo)

        # Botón para guardar
        save_button = QPushButton("Guardar")
        save_button.setStyleSheet("""
            background-color: #2ecc71;
            color: white;
            font: 12pt Arial;
            border-radius: 5px;
            padding: 10px;
        """)
        save_button.clicked.connect(self.guardar_usuario)
        layout.addWidget(save_button)

        # Guardar el user_id para el proceso de actualización
        self.user_id = user_id

    def guardar_usuario(self):
        """Guarda el usuario en la base de datos"""
        nombre = self.nombre_input.text().strip()
        correo = self.correo_input.text().strip()
        contraseña = self.password_input.text().strip()
        rol = self.role_combo.currentText()

        if nombre and correo and contraseña:
            try:
                # Conectar a la base de datos e insertar o modificar el usuario
                db = DBConnection()
                db.connect()

                # Verifica si el usuario tiene un Id para saber si es una modificación
                if self.user_id:
                    db.modificar_usuario(self.user_id, nombre, correo, contraseña, rol)
                else:
                    db.insertar_usuario(nombre, correo, contraseña, rol)

                db.close()

                # Mostrar un mensaje de éxito
                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("Éxito")
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setText("Usuario guardado exitosamente.")
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.setStyleSheet("""
                    QMessageBox {
                        font: 12pt Arial;
                        background-color: #d4efdf;
                    }
                    QPushButton {
                        background-color: #2ecc71;
                        color: white;
                        font: 12pt Arial;
                        border-radius: 5px;
                        padding: 5px;
                    }
                """)
                mensaje.exec_()
                self.accept()  # Cierra el formulario después de guardar
            except Exception as e:
                # Mostrar un mensaje de error si ocurre algo inesperado
                mensaje = QMessageBox(self)
                mensaje.setWindowTitle("Error")
                mensaje.setIcon(QMessageBox.Critical)
                mensaje.setText(f"Ocurrió un error al guardar el usuario:\n{e}")
                mensaje.setStandardButtons(QMessageBox.Ok)
                mensaje.exec_()
        else:
            self.mostrar_error()
