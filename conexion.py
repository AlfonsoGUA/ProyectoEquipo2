import mysql.connector

class DBConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        """Conectar a la base de datos"""
        self.conn = mysql.connector.connect(
            host="localhost",        
            user="root",             
            password='',  
            database="tienda"        
        )

    def fetch_productos(self):
        """Obtener productos desde la base de datos"""
        cursor = self.conn.cursor()
        query = "SELECT * FROM Productos"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def fetch_usuarios(self):
        """Obtener usuarios desde la base de datos"""
        cursor = self.conn.cursor()
        query = "SELECT * FROM Usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    
    def fetch_proveedores(self):
        """
        Obtiene todos los proveedores de la tabla Proveedores.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Proveedores")
        results = cursor.fetchall()
        cursor.close()
        return results

    def log(self, correo, contrasena):
        """
        Verifica si el usuario con el correo y contraseña dados existe en la base de datos.
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM Usuarios WHERE Correo = %s AND Contraseña = %s"
        cursor.execute(query, (correo, contrasena))
        user = cursor.fetchone()
        cursor.close()
        return user  # Retorna None si no se encuentra el usuario, o los datos del usuario si existe.


    def close(self):
        """Cerrar la conexión"""
        if self.conn:
            self.conn.close()
