class Persona:

    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
