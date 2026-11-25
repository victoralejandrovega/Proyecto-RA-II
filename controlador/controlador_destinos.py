from modelo import Destino


class ControladorDestinos:
    def __init__(self):
        self.destinos = []
        self.poblar_destinos()

    def poblar_destinos(self):
        # datos de la tabla de precios del enunciado
        self.destinos.append(Destino("Cochamó", 20000, 5000))
        self.destinos.append(Destino("Puelo Bajo", 20000, 5000))
        self.destinos.append(Destino("Contao", 20000, 5000))
        self.destinos.append(Destino("Rio Negro", 25000, 6000))
        self.destinos.append(Destino("Pupelde", 25000, 6000))
        self.destinos.append(Destino("Chepu", 30000, 8000))
        self.destinos.append(Destino("Ayacara", 30000, 8000))
        self.destinos.append(Destino("Pillán", 40000, 12000))
        self.destinos.append(Destino("Reñihue", 40000, 12000))
        self.destinos.append(Destino("Isla Quenac", 40000, 12000))
        self.destinos.append(Destino("Palqui", 40000, 12000))
        self.destinos.append(Destino("Chaitén", 50000, 15000))
        self.destinos.append(Destino("Santa Bárbara", 50000, 15000))

    def buscar_por_nombre(self, nombre):
        for d in self.destinos:
            if d.nombre.lower() == nombre.lower():
                return d
        return None
