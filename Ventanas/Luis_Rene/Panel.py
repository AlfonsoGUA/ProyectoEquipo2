# from PyQt5 import QtCore, QtGui, QtWidgets

# class VentanaHija(QtWidgets.QWidget):
#     def __init__(self, usuario, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Ventana Hija")
#         self.resize(784, 600)

#         # Frame principal
#         self.FramePrincipal = QtWidgets.QWidget(self)
#         self.FramePrincipal.setObjectName("FramePrincipal")

#         # Frame del usuario
#         self.FrameUsuario = QtWidgets.QFrame(self.FramePrincipal)
#         self.FrameUsuario.setGeometry(QtCore.QRect(0, 0, 241, 601))
#         self.FrameUsuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FrameUsuario.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FrameUsuario.setObjectName("FrameUsuario")

#         self.Usuario = QtWidgets.QLabel(self.FrameUsuario)
#         self.Usuario.setGeometry(QtCore.QRect(60, 40, 121, 41))
#         self.Usuario.setObjectName("Usuario")
#         self.Usuario.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{usuario}</span></p></body></html>")

#         # Botón Cerrar sesión
#         self.CerrarSesion = QtWidgets.QPushButton(self.FrameUsuario)
#         self.CerrarSesion.setGeometry(QtCore.QRect(60, 80, 131, 51))
#         self.CerrarSesion.setObjectName("CerrarSesion")
#         self.CerrarSesion.setText("Cerrar Sesión")

#         # Frame de acciones
#         self.FrameAccion = QtWidgets.QFrame(self.FrameUsuario)
#         self.FrameAccion.setGeometry(QtCore.QRect(0, 150, 241, 421))
#         self.FrameAccion.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FrameAccion.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FrameAccion.setObjectName("FrameAccion")

#         self.Usuarios = QtWidgets.QPushButton(self.FrameAccion)
#         self.Usuarios.setGeometry(QtCore.QRect(0, 0, 241, 71))
#         self.Usuarios.setObjectName("Usuarios")
#         self.Usuarios.setText("Usuarios")

#         self.Proveedores = QtWidgets.QPushButton(self.FrameAccion)
#         self.Proveedores.setGeometry(QtCore.QRect(0, 80, 241, 71))
#         self.Proveedores.setObjectName("Proveedores")
#         self.Proveedores.setText("Proveedores")

#         self.Productos = QtWidgets.QPushButton(self.FrameAccion)
#         self.Productos.setGeometry(QtCore.QRect(0, 160, 241, 71))
#         self.Productos.setObjectName("Productos")
#         self.Productos.setText("Productos")

#         self.Carrito = QtWidgets.QPushButton(self.FrameAccion)
#         self.Carrito.setGeometry(QtCore.QRect(0, 350, 241, 71))
#         self.Carrito.setObjectName("Carrito")
#         self.Carrito.setText("Carrito")

#         # Frame principal para las acciones
#         self.frame = QtWidgets.QFrame(self.FramePrincipal)
#         self.frame.setGeometry(QtCore.QRect(240, 0, 541, 601))
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")

#         # Establecer la ventana como el widget central
#         self.setLayout(QtWidgets.QVBoxLayout())
#         self.layout().addWidget(self.FramePrincipal)

#     def cerrar_sesion(self):
#         """Cerrar la ventana hija cuando se haga clic en 'Cerrar Sesión'."""
#         self.close()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ventana = VentanaHija(usuario="UsuarioEjemplo")  # Puedes pasar el nombre del usuario aquí
#     ventana.show()
#     sys.exit(app.exec_())
# from PyQt5 import QtCore, QtGui, QtWidgets

# class VentanaHija(QtWidgets.QWidget):
#     def __init__(self, usuario, main_window, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Ventana Hija")
#         self.resize(1000, 601)

#         self.main_window = main_window  # Ventana principal para regresar

#         Frame principal
#         self.FramePrincipal = QtWidgets.QWidget(self)
#         self.FramePrincipal.setObjectName("FramePrincipal")

#         Frame del usuario
#         self.FrameUsuario = QtWidgets.QFrame(self.FramePrincipal)
#         self.FrameUsuario.setGeometry(QtCore.QRect(0, 0, 241, 601))
#         self.FrameUsuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FrameUsuario.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FrameUsuario.setObjectName("FrameUsuario")
#         self.FrameUsuario.setStyleSheet("""
#             background-color: #005c99;
#             border-top-left-radius: 10px;
#             border-bottom-left-radius: 10px;
#         """)

#         self.Usuario = QtWidgets.QLabel(self.FrameUsuario)
#         self.Usuario.setGeometry(QtCore.QRect(60, 40, 121, 41))
#         self.Usuario.setObjectName("Usuario")
#         self.Usuario.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color: white;\">{usuario}</span></p></body></html>")

#         Botón Cerrar sesión
#         self.CerrarSesion = QtWidgets.QPushButton(self.FrameUsuario)
#         self.CerrarSesion.setGeometry(QtCore.QRect(60, 80, 131, 51))
#         self.CerrarSesion.setObjectName("CerrarSesion")
#         self.CerrarSesion.setText("Cerrar Sesión")
#         self.CerrarSesion.setStyleSheet("""
#             background-color: #003f73;
#             color: white;
#             border: none;
#             border-radius: 5px;
#             font-size: 14px;
#         """)
#         self.CerrarSesion.clicked.connect(self.cerrar_sesion)

#         Frame de acciones
#         self.FrameAccion = QtWidgets.QFrame(self.FrameUsuario)
#         self.FrameAccion.setGeometry(QtCore.QRect(0, 150, 851, 601))
#         self.FrameAccion.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FrameAccion.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FrameAccion.setObjectName("FrameAccion")

#         Botones de acciones con diseño
#         self.Usuarios = self.create_action_button("Usuarios", 0)
#         self.Proveedores = self.create_action_button("Proveedores", 80)
#         self.Productos = self.create_action_button("Productos", 160)
#         self.Carrito = self.create_action_button("Carrito", 350)

#         Frame principal para las acciones
#         self.frame = QtWidgets.QFrame(self.FramePrincipal)
#         self.frame.setGeometry(QtCore.QRect(240, 0, 841, 601))
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.frame.setStyleSheet("""
#             background-color: #afafaf;
#             border-top-right-radius: 10px;
#             border-bottom-right-radius: 10px;
#         """)

#         Establecer la ventana como el widget central
#         self.setLayout(QtWidgets.QVBoxLayout())
#         self.layout().addWidget(self.FramePrincipal)

#     def create_action_button(self, text, y_position):
#         button = QtWidgets.QPushButton(self.FrameAccion)
#         button.setGeometry(QtCore.QRect(0, y_position, 241, 71))
#         button.setObjectName(text)
#         button.setText(text)
#         button.setStyleSheet("""
#             background-color: #007bb5;
#             color: white;
#             border: none;
#             border-radius: 5px;
#             font-size: 14px;
#         """)
#         return button

#     def cerrar_sesion(self):
#         """Cerrar la ventana hija, limpiar los campos y regresar a la ventana principal."""

#         self.close()  # Cerrar la ventana hija
#         self.main_window.show()  # Mostrar la ventana principal nuevamente
#         self.main_window.raise_()  # Asegurarse de que la ventana principal esté al frente

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)

#     Crear ventana principal (puedes sustituir esto por tu clase Ui_MainWindow)
#     main_window = QtWidgets.QMainWindow()
#     main_window.setWindowTitle("Ventana Principal")
#     main_window.resize(800, 600)

#     Llamar a la ventana hija con el nombre de usuario
#     ventana = VentanaHija(usuario="UsuarioEjemplo", main_window=main_window)  # Pasar la ventana principal
#     ventana.show()

#     main_window.show()  # Mostrar la ventana principal al inicio

#     sys.exit(app.exec_())
# from PyQt5 import QtCore, QtGui, QtWidgets

# class VentanaHija(QtWidgets.QWidget):
#     def __init__(self, usuario, main_window, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Ventana Hija")
#         self.resize(1000, 601)

#         self.main_window = main_window  # Ventana principal para regresar

#         # Frame principal
#         self.FramePrincipal = QtWidgets.QWidget(self)
#         self.FramePrincipal.setObjectName("FramePrincipal")

#         # Frame del usuario
#         self.FrameUsuario = QtWidgets.QFrame(self.FramePrincipal)
#         self.FrameUsuario.setGeometry(QtCore.QRect(0, 0, 241, 601))
#         self.FrameUsuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FrameUsuario.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FrameUsuario.setObjectName("FrameUsuario")
#         self.FrameUsuario.setStyleSheet("""
#             background-color: #005c99;
#             border-top-left-radius: 10px;
#             border-bottom-left-radius: 10px;
#         """)

#         self.Usuario = QtWidgets.QLabel(self.FrameUsuario)
#         self.Usuario.setGeometry(QtCore.QRect(60, 40, 121, 41))
#         self.Usuario.setObjectName("Usuario")
#         self.Usuario.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color: white;\">{usuario}</span></p></body></html>")

#         # Botón Cerrar sesión
#         self.CerrarSesion = QtWidgets.QPushButton(self.FrameUsuario)
#         self.CerrarSesion.setGeometry(QtCore.QRect(60, 80, 131, 51))
#         self.CerrarSesion.setObjectName("CerrarSesion")
#         self.CerrarSesion.setText("Cerrar Sesión")
#         self.CerrarSesion.setStyleSheet("""
#             background-color: #003f73;
#             color: white;
#             border: none;
#             border-radius: 5px;
#             font-size: 14px;
#         """)
#         self.CerrarSesion.clicked.connect(self.cerrar_sesion)

#         # Frame de acciones
#         self.FrameAccion = QtWidgets.QFrame(self.FrameUsuario)
#         self.FrameAccion.setGeometry(QtCore.QRect(0, 150, 851, 601))
#         self.FrameAccion.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FrameAccion.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FrameAccion.setObjectName("FrameAccion")

#         # Botones de acciones con diseño
#         self.Usuarios = self.create_action_button("Usuarios", 0)
#         self.Proveedores = self.create_action_button("Proveedores", 80)
#         self.Productos = self.create_action_button("Productos", 160)
#         self.Carrito = self.create_action_button("Carrito", 350)

#         # Frame principal para las acciones
#         self.frame = QtWidgets.QFrame(self.FramePrincipal)
#         self.frame.setGeometry(QtCore.QRect(240, 0, 841, 601))
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frameAccion")
#         self.frame.setStyleSheet("""
#             background-color: #afafaf;
#             border-top-right-radius: 10px;
#             border-bottom-right-radius: 10px;
#         """)

#         # Establecer la ventana como el widget central
#         self.setLayout(QtWidgets.QVBoxLayout())
#         self.layout().addWidget(self.FramePrincipal)

#     def create_action_button(self, text, y_position):
#         button = QtWidgets.QPushButton(self.FrameAccion)
#         button.setGeometry(QtCore.QRect(0, y_position, 241, 71))
#         button.setObjectName(text)
#         button.setText(text)
#         button.setStyleSheet("""
#             background-color: #007bb5;
#             color: white;
#             border: none;
#             border-radius: 5px;
#             font-size: 14px;
#         """)
#         return button

#     def cerrar_sesion(self):
#         """Cerrar la ventana hija, limpiar los campos y regresar a la ventana principal."""

#         self.close()  # Cerrar la ventana hija
#         self.main_window.show()  # Mostrar la ventana principal nuevamente
#         self.main_window.raise_()  # Asegurarse de que la ventana principal esté al frente

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)

#     # Crear ventana principal (puedes sustituir esto por tu clase Ui_MainWindow)
#     main_window = QtWidgets.QMainWindow()
#     main_window.setWindowTitle("Ventana Principal")
#     main_window.resize(800, 600)

#     # Llamar a la ventana hija con el nombre de usuario
#     ventana = VentanaHija(usuario="UsuarioEjemplo", main_window=main_window)  # Pasar la ventana principal
#     ventana.show()

#     main_window.show()  # Mostrar la ventana principal al inicio

#     sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets

class VentanaHija(QtWidgets.QWidget):
    def __init__(self, usuario, db_connection, main_window, parent=None):
        super().__init__(parent)
        self.db_connection=db_connection
        self.setWindowTitle("Ventana Hija")
        self.resize(1000, 601)
        if self.db_connection:
            print("Conexión a la base de datos está activa.")
        else:
            print("No hay conexión a la base de datos.")

        self.main_window = main_window  # Ventana principal para regresar

        # Frame principal
        self.FramePrincipal = QtWidgets.QWidget(self)
        self.FramePrincipal.setObjectName("FramePrincipal")

        # Frame del usuario
        self.FrameUsuario = QtWidgets.QFrame(self.FramePrincipal)
        self.FrameUsuario.setGeometry(QtCore.QRect(0, 0, 241, 601))
        self.FrameUsuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameUsuario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameUsuario.setObjectName("FrameUsuario")
        self.FrameUsuario.setStyleSheet("""
            background-color: #005c99;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
        """)

        self.Usuario = QtWidgets.QLabel(self.FrameUsuario)
        self.Usuario.setGeometry(QtCore.QRect(60, 40, 121, 41))
        self.Usuario.setObjectName("Usuario")
        self.Usuario.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color: white;\">{usuario}</span></p></body></html>")

        # Botón Cerrar sesión
        self.CerrarSesion = QtWidgets.QPushButton(self.FrameUsuario)
        self.CerrarSesion.setGeometry(QtCore.QRect(60, 80, 131, 51))
        self.CerrarSesion.setObjectName("CerrarSesion")
        self.CerrarSesion.setText("Cerrar Sesión")
        self.CerrarSesion.setStyleSheet("""
            background-color: #003f73;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 14px;
        """)
        self.CerrarSesion.clicked.connect(self.cerrar_sesion)

        # Frame de acciones
        self.FrameAccion = QtWidgets.QFrame(self.FrameUsuario)
        self.FrameAccion.setGeometry(QtCore.QRect(0, 150, 851, 601))
        self.FrameAccion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameAccion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAccion.setObjectName("FrameAccion")

        # Botones de acciones con diseño
        self.Usuarios = self.create_action_button("Usuarios", 0)
        self.Usuarios.clicked.connect(self.mostrar_usuarios)
        self.Proveedores = self.create_action_button("Proveedores", 80)
        self.Productos = self.create_action_button("Productos", 160)
        self.Carrito = self.create_action_button("Carrito", 350)

        # Frame principal para las acciones
        self.frame = QtWidgets.QFrame(self.FramePrincipal)
        self.frame.setGeometry(QtCore.QRect(240, 0, 841, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frameAccion")
        self.frame.setStyleSheet("""
            background-color: #afafaf;
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        """)

        # Establecer el layout del frame
        self.frame.setLayout(QtWidgets.QVBoxLayout())

        # Establecer la ventana como el widget central
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.FramePrincipal)
        

    def create_action_button(self, text, y_position):
        button = QtWidgets.QPushButton(self.FrameAccion)
        button.setGeometry(QtCore.QRect(0, y_position, 241, 71))
        button.setObjectName(text)
        button.setText(text)
        button.setStyleSheet("""
            background-color: #007bb5;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 14px;
        """)
        return button
    def mostrar_usuarios(self):
        """Muestra la tabla de usuarios en el FrameAccion ocupando todo el espacio disponible."""
        self.limpiar_frame()  # Limpiar el frame antes de agregar la tabla

        # Crear la tabla
        table_widget = QtWidgets.QTableWidget(self.frame)
        table_widget.setColumnCount(4)  # 4 columnas: ID, Nombre, Correo, Rol
        table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Correo", "Rol"])
        table_widget.setStyleSheet("""
        QTableWidget {
            background-color: #ffffff;
            border: none;
            gridline-color: #cccccc;
        }
        QHeaderView::section {
            background-color: #007bb5;
            color: white;
            font-weight: bold;
            border: none;
            text-align: center;
        }
        QTableWidget::item {
            border: none;
            text-align: center;
        }
        QTableWidget::item:selected {
            background-color: #dceffd;
            color: black;
        }
    """)
        table_widget.setAlternatingRowColors(True)  # Colores alternados en filas
        table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Desactivar edición
        table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Selección por fila
        table_widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # Selección única

        # Ajustar la tabla al tamaño del frame
        table_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        try:
        # Consultar los usuarios desde la base de datos
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id_Usuario, nombre, correo, rol FROM usuarios")
            usuarios = cursor.fetchall()
            table_widget.setRowCount(len(usuarios))

            for row, usuario in enumerate(usuarios):
                for col, dato in enumerate(usuario):
                    table_widget.setItem(row, col, QtWidgets.QTableWidgetItem(str(dato)))

        # Ajustar las columnas para ocupar todo el ancho del widget
            table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        except Exception as e:
            print(f"Error al cargar usuarios: {e}")
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudieron cargar los usuarios.")

    # Agregar la tabla al layout del frame
        self.frame.layout().addWidget(table_widget)
    def limpiar_frame(self):
        """Limpiar el Frame para agregar una nueva funcionalidad"""
        for i in reversed(range(self.frame.layout().count())):
            widget = self.frame.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def cerrar_sesion(self):
        """Cerrar la ventana hija, limpiar los campos y regresar a la ventana principal."""
        self.close()  # Cerrar la ventana hija
        #self.db_connection.ce
        self.main_window.show()  # Mostrar la ventana principal nuevamente
        self.main_window.raise_()  # Asegurarse de que la ventana principal esté al frente


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Crear ventana principal (puedes sustituir esto por tu clase Ui_MainWindow)
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle("Ventana Principal")
    main_window.resize(800, 600)

    # Llamar a la ventana hija con el nombre de usuario
    ventana = VentanaHija(usuario="UsuarioEjemplo", main_window=main_window)  # Pasar la ventana principal
    ventana.show()

    main_window.show()  # Mostrar la ventana principal al inicio

    sys.exit(app.exec_())
