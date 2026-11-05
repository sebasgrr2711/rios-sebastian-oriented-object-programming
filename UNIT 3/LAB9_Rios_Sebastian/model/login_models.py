from controller.connection_db import Database_connection

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = Database_connection()

    def auth(self):

        query = "SELECT id_user, username, nombre FROM users WHERE username = %s AND password = %s"

        result = self.db.ejecutar_consulta(query,(self.username, self.password))
    
        return result