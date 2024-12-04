from qtpy.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget
from qtpy.QtCore import Qt
from conexion import DBConnection  
from Usuarios import UsuariosView
from Proveedores import ProveedoresView
from Productos import ProductosView
from Tienda import TiendaView

class TiendaMenu(QMainWindow):
    def __init__(self, usuario, login_window, parent=None):
        super().__init__(parent)
        self.login_window = login_window  
        self.usuario = usuario  

        # Conexión a la base de datos
        self.db = DBConnection()
        self.db.connect()
        
        # Obtener el nombre del usuario y rol
        self.nombre_usuario = self.db.get_user_name(self.usuario)
        self.rol_usuario = self.get_user_role(self.usuario)  # Consulta adicional para obtener el rol
        
        if not self.nombre_usuario:
            self.nombre_usuario = "Usuario desconocido" 

        self.setWindowTitle("Menú Principal")
        self.setGeometry(100, 100, 1200, 800)
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

        # Mostrar el nombre del usuario
        user_label = QLabel(self.nombre_usuario, side_menu)
        user_label.setStyleSheet("color: white; font: bold 16pt Arial; margin-top: 20px;")
        user_label.setAlignment(Qt.AlignCenter)
        side_menu_layout.addWidget(user_label)

        # Botón de cerrar sesión
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

        # Botones del menú según el rol
        if self.rol_usuario == "admin":
            admin_buttons = [
                ("Usuarios", self.show_usuarios),
                ("Productos", self.show_productos),
                ("Proveedores", self.show_proveedores),
            ]
            for text, command in admin_buttons:
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

        # Botón siempre visible: "Tienda" y "Carrito"
        general_buttons = [
            ("Tienda", self.show_tienda),
            ("Carrito", self.show_carrito),
        ]
        for text, command in general_buttons:
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

        # Área principal
        self.main_area = QStackedWidget(self)
        self.main_area.setStyleSheet("background-color: #ffffff; border-radius: 10px; padding: 20px;")

        main_layout.addWidget(side_menu)
        main_layout.addWidget(self.main_area)

        self.main_area_content = QLabel("Bienvenidos a la ferretería del Equipo 2", self)
        self.main_area_content.setStyleSheet("font: bold 18pt Arial; color: #2c3e50; text-align: center;")
        self.main_area.addWidget(self.main_area_content)

    def get_user_role(self, email):
        """Consulta el rol del usuario basado en su correo."""
        cursor = self.db.conn.cursor()
        query = "SELECT rol FROM usuarios WHERE correo = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else "usuario"  # Retorna 'usuario' por defecto si no se encuentra el rol

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
        self._clear_main_area()
        tienda_view = TiendaView()
        self.main_area.addWidget(tienda_view)
    
    def show_carrito(self):
        self.update_main_area("Carrito de Compras")

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
