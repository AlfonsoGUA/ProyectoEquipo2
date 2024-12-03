import sys
import mysql.connector
from PyQt5 import QtCore, QtWidgets
from Conexion.conexion import *
from Ventanas.Luis_Rene.Panel import *

# class Ui_MainWindow:
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("Login")
#         MainWindow.resize(400, 300)
#         MainWindow.setStyleSheet("""
#             QMainWindow {
#                 background-color: #FFFFFF;
#             }
#             QFrame {
#                 background-color: #FFFFFF;
#             }
#             QLabel {
#                 color: #005c99;
#                 font-size: 14px;
#             }
#             QPushButton {
#                 background-color: #005c99;
#                 color: white;
#                 border-radius: 5px;
#                 padding: 10px;
#                 font-size: 12px;
#             }
#             QPushButton:hover {
#                 background-color: #003f73;
#             }
#             QLineEdit {
#                 border: 1px solid #005c99;
#                 padding: 5px;
#             }
#             QLineEdit:focus {
#                 border-color: #003f73;
#             }
#         """)
        
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")

#         self.LabelUsuario = QtWidgets.QLabel(self.centralwidget)
#         self.LabelUsuario.setGeometry(QtCore.QRect(50, 50, 71, 40))
#         self.LabelUsuario.setObjectName("LabelUsuario")
#         self.LabelUsuario.setText("Usuario:")  # Añadir texto

#         self.LabelPass = QtWidgets.QLabel(self.centralwidget)
#         self.LabelPass.setGeometry(QtCore.QRect(50, 100, 71, 40))
#         self.LabelPass.setObjectName("LabelPass")
#         self.LabelPass.setText("Contraseña:")

#         self.TextUsuario = QtWidgets.QLineEdit(self.centralwidget)
#         self.TextUsuario.setGeometry(QtCore.QRect(130, 50, 200, 40))
#         self.TextUsuario.setObjectName("TextUsuario")

#         self.TextPass = QtWidgets.QLineEdit(self.centralwidget)
#         self.TextPass.setGeometry(QtCore.QRect(130, 100, 200, 40))
#         self.TextPass.setObjectName("TextPass")
#         self.TextPass.setEchoMode(QtWidgets.QLineEdit.Password)

#         self.BtnLogin = QtWidgets.QPushButton(self.centralwidget)
#         self.BtnLogin.setGeometry(QtCore.QRect(130, 150, 200, 40))
#         self.BtnLogin.setObjectName("BtnLogin")
#         self.BtnLogin.setText("Ingresar")

#         MainWindow.setCentralWidget(self.centralwidget)

#         self.db = TiendaDB(host="localhost", user="root", password="", database="Tienda")
#         self.db.conectar()

#         self.BtnLogin.clicked.connect(self.handle_login)
#     def open_child_window(self, usuario):
#         """Abrir una ventana hija."""
#         self.child_window = VentanaHija(usuario)
#         self.child_window.show()

#     def handle_login(self):
#         """Manejar el evento de inicio de sesión."""
#         usuario = self.TextUsuario.text().strip()
#         password = self.TextPass.text().strip()

#         if not usuario or not password:
#             QtWidgets.QMessageBox.warning(None, "Advertencia", "Por favor ingrese usuario y contraseña.")
#             return

#         if self.db.log(usuario, password):
#             QtWidgets.QMessageBox.information(None, "Éxito", f"Bienvenido, {usuario}!")
#             self.open_child_window(usuario)
#             MainWindow.hide()
            

#         else:
#             QtWidgets.QMessageBox.critical(None, "Error", "Credenciales incorrectas.")

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Login")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }
            QFrame {
                background-color: #FFFFFF;
            }
            QLabel {
                color: #005c99;
                font-size: 14px;
            }
            QPushButton {
                background-color: #005c99;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #003f73;
            }
            QLineEdit {
                border: 1px solid #005c99;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color: #003f73;
            }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LabelUsuario = QtWidgets.QLabel(self.centralwidget)
        self.LabelUsuario.setGeometry(QtCore.QRect(50, 50, 71, 40))
        self.LabelUsuario.setObjectName("LabelUsuario")
        self.LabelUsuario.setText("Usuario:")  # Añadir texto

        self.LabelPass = QtWidgets.QLabel(self.centralwidget)
        self.LabelPass.setGeometry(QtCore.QRect(50, 100, 71, 40))
        self.LabelPass.setObjectName("LabelPass")
        self.LabelPass.setText("Contraseña:")

        self.TextUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.TextUsuario.setGeometry(QtCore.QRect(130, 50, 200, 40))
        self.TextUsuario.setObjectName("TextUsuario")

        self.TextPass = QtWidgets.QLineEdit(self.centralwidget)
        self.TextPass.setGeometry(QtCore.QRect(130, 100, 200, 40))
        self.TextPass.setObjectName("TextPass")
        self.TextPass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.BtnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.BtnLogin.setGeometry(QtCore.QRect(130, 150, 200, 40))
        self.BtnLogin.setObjectName("BtnLogin")
        self.BtnLogin.setText("Ingresar")

        MainWindow.setCentralWidget(self.centralwidget)

        self.db = TiendaDB(host="localhost", user="root", password="", database="Tienda")
        self.db.conectar()

        self.BtnLogin.clicked.connect(self.handle_login)
    def clear_fields(self):
            """Limpiar los campos de texto de la ventana principal."""
            self.TextUsuario.clear()
            self.TextPass.clear()

    def open_child_window(self, usuario):
        """Abrir una ventana hija y pasar la ventana principal y la conexión a la base de datos."""
        self.child_window = VentanaHija(usuario, self.db, MainWindow)  # Pasar db aquí
        self.child_window.show()

    def handle_login(self):
        """Manejar el evento de inicio de sesión."""
        usuario = self.TextUsuario.text().strip()
        password = self.TextPass.text().strip()

        if not usuario or not password:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "Por favor ingrese usuario y contraseña.")
            return

        if self.db.log(usuario, password):
            QtWidgets.QMessageBox.information(None, "Éxito", f"Bienvenido, {usuario}!")
            self.open_child_window(usuario)
            self.clear_fields()
            MainWindow.hide()  # Ocultar la ventana principal al iniciar sesión

        else:
            QtWidgets.QMessageBox.critical(None, "Error", "Credenciales incorrectas.")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

