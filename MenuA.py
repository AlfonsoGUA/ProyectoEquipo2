from qtpy.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget
from qtpy.QtCore import Qt

from Usuarios import UsuariosView
from Proveedores import ProveedoresView
from Productos import ProductosView

class TiendaMenu(QMainWindow):
    def __init__(self, login_window, parent=None):
        super().__init__(parent)
        self.login_window = login_window  # Guardar referencia de la ventana de inicio de sesión

        self.setWindowTitle("Menú Principal")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("""
            background-color: #ecf0f1;
            font-family: 'Arial', sans-serif;
        """)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Menú lateral
        side_menu = QFrame(self)
        side_menu.setStyleSheet("background-color: #34495e; border-right: 2px solid #bdc3c7;")
        side_menu.setFixedWidth(250)

        side_menu_layout = QVBoxLayout(side_menu)
        side_menu_layout.setSpacing(20)

        user_label = QLabel("Menú de Navegación", side_menu)
        user_label.setStyleSheet("color: white; font: bold 16pt Arial; margin-top: 20px;")
        side_menu_layout.addWidget(user_label)

        logout_button = QPushButton("Cerrar sesión", side_menu)
        logout_button.setStyleSheet("""
            background-color: #e74c3c; 
            color: white; 
            font: bold 12pt Arial; 
            border-radius: 5px;
            padding: 10px;
        """)
        logout_button.clicked.connect(self.logout)
        side_menu_layout.addWidget(logout_button)

        menu_buttons = [
            ("Usuarios", self.show_usuarios),
            ("Productos", self.show_productos),
            ("Proveedores", self.show_proveedores),
            ("Tienda", self.show_tienda)
        ]
        for text, command in menu_buttons:
            btn = QPushButton(text, side_menu)
            btn.setStyleSheet("""
                background-color: #2c3e50; 
                color: white; 
                font: 12pt Arial; 
                padding: 12px;
                border-radius: 5px;
                margin-top: 10px;
            """)
            btn.clicked.connect(command)
            side_menu_layout.addWidget(btn)

        cart_button = QPushButton("Carrito", side_menu)
        cart_button.setStyleSheet("""
            background-color: #f1c40f; 
            color: white; 
            font: bold 14pt Arial; 
            border-radius: 5px;
            padding: 10px;
            margin-top: 20px;
        """)
        side_menu_layout.addWidget(cart_button)

        self.main_area = QStackedWidget(self)
        self.main_area.setStyleSheet("background-color: #ffffff; border-radius: 10px; padding: 20px;")

        main_layout.addWidget(side_menu)
        main_layout.addWidget(self.main_area)

        self.main_area_content = QLabel("Bienvenidos a la ferretería del Equipo 2", self)
        self.main_area_content.setStyleSheet("font: bold 18pt Arial; color: #2c3e50; text-align: center;")
        self.main_area.addWidget(self.main_area_content)
            

    def show_usuarios(self):
        self._clear_main_area()
        usuarios_view = UsuariosView()
        self.main_area.addWidget(usuarios_view)

    def show_productos(self):
        self._clear_main_area()
        productos_view = ProductosView()
        self.main_area.addWidget(productos_view)

    def show_proveedores(self):
        self._clear_main_area()
        proveedores_view = ProveedoresView()
        self.main_area.addWidget(proveedores_view)

    def show_tienda(self):
        self.update_main_area("Gestión de Tienda")

    def _clear_main_area(self):
        for i in range(self.main_area.count()):
            widget = self.main_area.widget(i)
            widget.deleteLater()

    def update_main_area(self, text):
        self._clear_main_area()
        label = QLabel(text, self)
        label.setStyleSheet("""
            font: bold 16pt Arial;
            color: #2c3e50;
            text-align: center;
        """)
        self.main_area.addWidget(label)

    def logout(self):
        """Cerrar sesión y volver a la ventana de inicio de sesión."""
        self.close()  # Cerrar la ventana actual
        self.login_window.show()  # Mostrar la ventana de inicio de sesión
