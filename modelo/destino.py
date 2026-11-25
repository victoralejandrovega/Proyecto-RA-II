class Destino:
    def __init__(self, nombre, precio_pasaje, precio_encomienda):
        self.nombre = nombre
        self.precio_pasaje = precio_pasaje            # por persona
        self.precio_encomienda = precio_encomienda    # por kg

    def __str__(self):
        return self.nombre
