# productos.py
# Define la clase Producto, que representa un ítem en la tienda

class Producto:
    """
    Clase que representa un producto en la tienda.
    Atributos:
        id_producto (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Cantidad disponible en inventario.
    """

    def __init__(self, id_producto, nombre, precio, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"

    def reducir_stock(self, cantidad):
        """Reduce el stock del producto si hay suficiente disponibilidad."""
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"Stock insuficiente para {self.nombre}. Disponible: {self.stock}")
            return False