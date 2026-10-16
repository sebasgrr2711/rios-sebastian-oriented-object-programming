from controller.connection_db import Database_connection


class Product:
    def __init__(self, id=None, nombre=None, precio=None, stock=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.db = Database_connection()

    def get_products(self):
        query = "SELECT * FROM products"
        return self.db.ejecutar_consulta(query)

    def add_product(self, name, price, stock):
        try:
            # Convertimos a tipos numéricos adecuados
            price = float(price)
            stock = int(stock)

            query = "INSERT INTO products (nombre, precio, stock) VALUES (%s, %s, %s)"
            self.db.ejecutar_consulta(query, (name, price, stock))
            return True
        except ValueError:
            print("Error: El precio debe ser un número y el stock un entero.")
            return False

    def refresh_table(self):
        return self.get_products()
