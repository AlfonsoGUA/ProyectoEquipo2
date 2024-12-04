import mysql.connector

class DBConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        """Conecta a la base de datos."""
        self.conn = mysql.connector.connect(
            host="localhost",       # Dirección del servidor de base de datos
            user="root",            # Usuario de la base de datos
            password='',            # Contraseña del usuario
            database="tienda"       # Nombre de la base de datos
        )

    def insertar_usuario(self, nombre, correo, contraseña, rol):
        """Inserta un nuevo usuario en la tabla Usuarios."""
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Usuarios (Nombre, Correo, Contraseña, Rol)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, correo, contraseña, rol))
            self.conn.commit()
            cursor.close()
        except mysql.connector.IntegrityError as err:
            if "Duplicate entry" in str(err):
                raise Exception("El correo ya está registrado.")
            else:
                raise Exception(f"Error al insertar el usuario: {err}")

    def validar_correo_existente(self, correo):
        """Valida si un correo ya existe en la base de datos."""
        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM Usuarios WHERE Correo = %s"
        cursor.execute(query, (correo,))
        existe = cursor.fetchone()[0] > 0
        cursor.close()
        return existe

    def get_user_name(self, email):
        """Consulta el nombre del usuario basado en el correo."""
        cursor = self.conn.cursor()
        query = "SELECT Nombre FROM Usuarios WHERE Correo = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None

    def fetch_productos(self):
        """Obtiene todos los productos de la tabla Productos."""
        cursor = self.conn.cursor()
        query = "SELECT * FROM Productos"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def fetch_usuarios(self):
        """Obtiene todos los usuarios de la tabla Usuarios."""
        cursor = self.conn.cursor()
        query = "SELECT * FROM Usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def fetch_proveedores(self):
        """Obtiene todos los proveedores de la tabla Proveedores."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Proveedores")
        results = cursor.fetchall()
        cursor.close()
        return results

    def log(self, correo, contrasena):
        """Verifica si un usuario con el correo y contraseña dados existe en la base de datos."""
        cursor = self.conn.cursor()
        query = "SELECT * FROM Usuarios WHERE Correo = %s AND Contraseña = %s"
        cursor.execute(query, (correo, contrasena))
        user = cursor.fetchone()
        cursor.close()
        return user

    class DBConnection:
        def __init__(self):
            self.conn = None

    def connect(self):
        """Conecta a la base de datos."""
        self.conn = mysql.connector.connect(
            host="localhost",       # Dirección del servidor de base de datos
            user="root",            # Usuario de la base de datos
            password='',            # Contraseña del usuario
            database="tienda"       # Nombre de la base de datos
        )

  # Método para modificar un usuario
    def modificar_usuario(self, user_id, nombre, correo, contraseña, rol):
        try:
            cursor = self.conn.cursor()
            query = """
                UPDATE Usuarios
                SET Nombre = %s, Correo = %s, Contraseña = %s, Rol = %s
                WHERE Id_Usuario = %s
            """
            cursor.execute(query, (nombre, correo, contraseña, rol, user_id))
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Detalles del error: {err}")  # Agregar detalles del error
            raise Exception(f"Error al modificar el usuario: {err}")
    # Otros métodos que ya tenías...

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.conn:
            self.conn.close()



    def delete_usuario(self, user_id):
        """Elimina un usuario de la base de datos por su ID"""
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM Usuarios WHERE Id_Usuario = %s"  # Cambio de 'Id' a 'Id_Usuario'
            cursor.execute(query, (user_id,))
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Detalles del error: {err}")
            raise Exception(f"Error al eliminar el usuario: {err}")

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.conn:
            self.conn.close()
