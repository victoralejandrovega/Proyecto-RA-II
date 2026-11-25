from modelo.persona import Persona


class Cliente(Persona):
    def __init__(self, rut, nombre, telefono, cantidad_vuelos=0):
        super().__init__(rut, nombre)
        self.telefono = telefono
        self.cantidad_vuelos = cantidad_vuelos  # vuelos que ya ha realizado

    def sumar_vuelo(self):
        self.cantidad_vuelos += 1

    def es_frecuente(self):
        # tiene 10% de descuento si ha realizado mas de 10 vuelos
        return self.cantidad_vuelos > 10
