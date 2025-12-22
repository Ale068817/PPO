# carrito.py
# Define la clase Carrito, que gestiona los productos seleccionados por un cliente

from Productos import Producto


class Carrito:
    """
    Clase que representa un carrito de compras.
    Atributos:
        items (dict): Diccionario con productos y sus cantidades.
    """

    def __init__(self):
        self.items = {}  # clave: Producto, valor: cantidad

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito si hay stock disponible."""
        if producto.reducir_stock(cantidad):
            if producto in self.items:
                self.items[producto] += cantidad
            else:
                self.items[producto] = cantidad
            print(f"Agregado {cantidad}x {producto.nombre} al carrito.")
        else:
            print(f"No se pudo agregar {producto.nombre} al carrito.")

    def mostrar_carrito(self):
        """Muestra todos los productos en el carrito y el total."""
        if not self.items:
            print("El carrito está vacío.")
            return 0

        total = 0
        print("\n--- Carrito de Compras ---")
        for producto, cantidad in self.items.items():
            subtotal = producto.precio * cantidad
            total += subtotal
            print(f"{producto.nombre} x{cantidad} = ${subtotal:.2f}")
        print(f"Total: ${total:.2f}\n")
        return total

    def vaciar(self):
        """Vacía el carrito."""
        self.items.clear()
        print("Carrito vaciado.")