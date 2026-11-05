import mysql.connector
from mysql.connector import Error
from controller.config import DB_config

class Database_connection:
    def __init__(self):
         self.config = DB_config

    def get_connection(self):
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
            conexion = self.get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(dictionary=True)
            try:
                cursor.execute(query, params)
                resultados = cursor.fetchall()
                return resultados
            except Error as e:
                print(f"Error en la consulta SQL: {e}")
                return None
            finally:
                if conexion.is_connected():
                    cursor.close()
                    conexion.close()