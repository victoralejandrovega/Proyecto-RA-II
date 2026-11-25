from modelo.asiento import Asiento


class Vuelo:
    def __init__(self, codigo, destino, avion, fecha, hora, extraordinario=False):
        self.codigo = codigo
        self.destino = destino
        self.avion = avion
        self.fecha = fecha
        self.hora = hora
        self.extraordinario = extraordinario
        self.carga_usada_kg = 0

        # se crean tantos asientos como capacidad tenga el avion
        self.asientos = []
        for i in range(1, avion.capacidad_pasajeros + 1):
            self.asientos.append(Asiento(i))

    def asientos_libres(self):
        libres = 0
        for a in self.asientos:
            if not a.ocupado:
                libres += 1
        return libres

    def reservar_asiento(self, numero):
        # reserva un asiento por su numero, y devuelve False si no se pudo
        for a in self.asientos:
            if a.numero == numero and not a.ocupado:
                a.ocupado = True
                return True
        return False

    def carga_disponible_kg(self):
        return self.avion.capacidad_carga_kg - self.carga_usada_kg

    def agregar_carga(self, kg):
        # agrega una encomienda si cabe en el avio
        if kg <= self.carga_disponible_kg():
            self.carga_usada_kg += kg
            return True
        return False
