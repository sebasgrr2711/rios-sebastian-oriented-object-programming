from controller.connection_db import Database_connection


class Product:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def get_products(self):
        query = "SELECT * FROM products"
        return self.db.ejecutar_consulta(query)
