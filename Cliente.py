# cliente.py
# Define la clase Cliente, que representa a un usuario de la tienda

class Cliente:
    """
    Clase que representa a un cliente de la tienda.
    Atributos:
        nombre (str): Nombre del cliente.
        email (str): Correo electrónico del cliente.
    """

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email})"