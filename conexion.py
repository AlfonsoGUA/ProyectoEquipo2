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
        query = "SELECT Nombre, Precio, Id_Proveedor FROM Productos LIMIT 6"
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

    def close(self):
        """Cerrar la conexión"""
        if self.conn:
            self.conn.close()
