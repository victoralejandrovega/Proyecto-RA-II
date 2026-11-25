from modelo.avion import Avion


class Cessna310(Avion):
    def __init__(self):
        super().__init__("CESSNA 310", 5, 910)
