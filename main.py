
from datetime import date

from modelo import Gerente, Asistente, Cliente, Pasaje, Encomienda, Venta
from controlador import ControladorDestinos, ControladorVuelos
from vista import VistaConsola


def main():
    # se crean los objetos del MVC
    vista = VistaConsola()
    ctrl_destinos = ControladorDestinos()   # crea los destinos
    ctrl_vuelos = ControladorVuelos()

    # poblamiento de datos, un vuelo diario a cada destino durante 3 dias
    hoy = date(2026, 11, 26)
    ctrl_vuelos.poblar_vuelos(ctrl_destinos.destinos, hoy, 3)

    # se crean otros objetos del modelo
    gerente = Gerente("11.111.111-1", "Carlos Soto")
    asistente = Asistente("22.222.222-2", "Marta Vera")
    cliente = Cliente("12.345.678-9", "Juan Pérez", "+56911111111", 3)

    vuelo = ctrl_vuelos.vuelos[0]
    pasaje = Pasaje(cliente, vuelo, 1, 20000)
    encomienda = Encomienda(cliente, vuelo, 12.5, 62500)
    venta = Venta(1, hoy, "Pasaje", "Pasaje AC-001 asiento 1", "Efectivo", 20000)

    # se muestran los datos
    vista.mostrar_mensaje(f"Gerente: {gerente}")
    vista.mostrar_mensaje(f"Asistente: {asistente}")
    vista.mostrar_mensaje(f"Cliente: {cliente}")
    vista.mostrar_destinos(ctrl_destinos.destinos)
    vista.mostrar_vuelos(ctrl_vuelos.vuelos)
    vista.mostrar_mensaje(f"Total de vuelos creados: {len(ctrl_vuelos.vuelos)}")


if __name__ == "__main__":
    main()
