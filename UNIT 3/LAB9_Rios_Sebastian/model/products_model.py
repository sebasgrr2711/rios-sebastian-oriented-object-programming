from controller.connection_db import Database_connection

class ProductModel:
    def __init__(self):
        self.db = Database_connection()

    def get_all_products(self):
        query = "SELECT id_product, nombre, precio, stock FROM products"
        return self.db.ejecutar_consulta(query)

    def add_product(self, nombre, precio, stock):
        query = "INSERT INTO products (nombre, precio, stock) VALUES (%s, %s, %s)"
        conexion = self.db.get_connection()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(query, (nombre, precio, stock))
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
            except Exception as e:
                print(f"Error al guardar producto: {e}")
                return False
        return False