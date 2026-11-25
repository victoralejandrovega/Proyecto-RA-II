class Venta:
    def __init__(self, id, fecha, tipo_servicio, detalle, medio_pago, monto):
        self.id = id
        self.fecha = fecha
        self.tipo_servicio = tipo_servicio  # "Pasaje" o "Encomienda"
        self.detalle = detalle
        self.medio_pago = medio_pago
        self.monto = monto
