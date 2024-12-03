import sys
import mysql.connector
from PyQt5 import QtCore, QtWidgets

class TiendaDB:
    def __init__(self, host, user, password, database):
        """Inicializa la conexión a la base de datos."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        """Establece la conexión con la base de datos."""
        print("Intentando conectar a la base de datos...")
        if self.connection and self.connection.is_connected():
            print("Ya hay una conexión establecida.")
            return

        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        print("Conexión exitosa a la base de datos.")
    def cursor(self):
        return self.connection.cursor()
    def log(self, usuario, password):
        """Valida las credenciales del usuario."""
        if not self.connection or not self.connection.is_connected():
            print("Conexión no establecida. Intentando reconectar...")
            self.conectar()

        if not self.connection or not self.connection.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return False

        print("Ejecutando la consulta de login...")
        with self.connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM Usuarios WHERE Nombre = %s AND Contraseña = %s"
            cursor.execute(query, (usuario, password))
            result = cursor.fetchone()
            print(f"Resultado de la consulta: {result}")
            return result is not None
    def obtener_usuarios(self):
        """Obtiene todos los usuarios de la base de datos."""
        if not self.connection or not self.connection.is_connected():
            print("Conexión no establecida. Intentando reconectar...")
            self.conectar()

        if not self.connection or not self.connection.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return []

if __name__ == "__main__":
    # Crear instancia de conexión a la base de datos
    db = TiendaDB(host="localhost", user="root", password="", database="Tienda")

    # Intentar conectar a la base de datos
    try:
        db.conectar()

        # Definir usuario y contraseña para prueba
        usuario = "Luis Rene"  # Asegúrate de tener este usuario en la base de datos
        password = "123456"  # Contraseña correspondiente

        # Intentar hacer login
        if db.log(usuario, password):
            print(f"Login exitoso para {usuario}")
        else:
            print(f"Credenciales incorrectas para {usuario}")

    except Exception as e:
        print(f"Error crítico: {e}")
    finally:
        db.cerrar_conexion()
