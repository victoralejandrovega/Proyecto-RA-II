from datetime import timedelta
from modelo import Vuelo, Cessna310, Cessna208Caravan, Let410


class ControladorVuelos:
    def __init__(self):
        self.vuelos = []
        self.contador_codigo = 1

    def poblar_vuelos(self, destinos, fecha_inicio, cantidad_dias):
   
        horas = ["08:00", "09:00", "10:00", "11:00", "12:00", "14:00", "15:00"]

        for dia in range(cantidad_dias):
            fecha = fecha_inicio + timedelta(days=dia)
            i = 0
            for d in destinos:
                if d.precio_pasaje <= 20000:
                    avion = Cessna310()
                elif d.precio_pasaje <= 30000:
                    avion = Cessna208Caravan()
                else:
                    avion = Let410()
                hora = horas[i % len(horas)]
                codigo = f"AC-{self.contador_codigo:03d}"
                self.contador_codigo += 1
                self.vuelos.append(Vuelo(codigo, d, avion, fecha, hora))
                i += 1
