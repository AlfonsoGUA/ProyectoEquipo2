import sys
from PyQt5 import QtCore, QtWidgets
from conexion import DBConnection

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
                color:  #34495e;
                font-size: 14px;
            }
            QPushButton {
                background-color: #34495e;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color:  #e74c3c;
            }
            QLineEdit {
                border: 1px solid  #34495e;
                padding: 5px;
            }
            QLineEdit:focus {
                border-color:  #e74c3c;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LabelUsuario = QtWidgets.QLabel(self.centralwidget)
        self.LabelUsuario.setGeometry(QtCore.QRect(50, 50, 71, 40))
        self.LabelUsuario.setObjectName("LabelUsuario")
        self.LabelUsuario.setText("Usuario:")

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

        
        self.db = DBConnection()
        try:
            self.db.connect()  
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Error al conectar a la base de datos:\n{str(e)}")
            sys.exit()

        self.BtnLogin.clicked.connect(self.handle_login)

    def handle_login(self):
        """Manejar el evento de inicio de sesión."""
        correo = self.TextUsuario.text().strip()
        contrasena = self.TextPass.text().strip()

        if not correo or not contrasena:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "Por favor ingrese correo y contraseña.")
            return

       
        user = self.db.log(correo, contrasena)
        if user:
            QtWidgets.QMessageBox.information(None, "Éxito", f"Bienvenido, {user[1]}!")  
            self.clear_fields()
            self.open_menu_window(correo)  
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "Correo o contraseña incorrectos.")


    def open_menu_window(self,correo):
        """Abrir la ventana del menú principal."""
        from MenuA import TiendaMenu  
        self.menu_window = TiendaMenu(correo,MainWindow)  
        self.menu_window.show()  
        MainWindow.hide()  
    def clear_fields(self):
            """Limpiar los campos de texto de la ventana principal."""
            self.TextUsuario.clear()
            self.TextPass.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())