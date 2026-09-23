from abc import ABC, abstractmethod


# ABSTRACCIÓN
class Producto(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_precio(self):
        pass


# PRODUCTOS CONCRETOS

class Electronico(Producto):

    def calcular_precio(self):
        return self.precio * 1.16


class Ropa(Producto):

    def calcular_precio(self):
        return self.precio * 1.08


class Alimento(Producto):

    def calcular_precio(self):
        return self.precio


# PEDIDO

class Pedido:

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):

        total = 0

        for producto in self.productos:
            total += producto.calcular_precio()

        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):

        print("\nPedido #", self.numero)
        print("Cliente:", self.cliente)
        print("Estado:", self.estado)

        print("\nProductos:")

        for producto in self.productos:
            print("-", producto.nombre)
            print("Precio:", producto.calcular_precio())

        print("\nTotal:", self.calcular_total())


# MAIN PROGRAM

pedido = Pedido(1001, "Ana")

pedido.agregar_producto(
    Electronico("Laptop", 15000)
)

pedido.agregar_producto(
    Ropa("Playera", 500)
)

pedido.agregar_producto(
    Alimento("Cereal", 100)
)

pedido.mostrar_pedido()

pedido.cambiar_estado("ENVIADO")

print("\nNuevo estado:", pedido.estado)
