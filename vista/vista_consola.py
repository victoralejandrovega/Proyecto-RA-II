class VistaConsola:

    def _pesos(self, monto):
        return "$" + f"{monto:,.0f}".replace(",", ".")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_destinos(self, destinos):
        print("=== DESTINOS ===")
        print(f"{'Destino':<15} {'Pasaje':<12} {'Encomienda/kg':<12}")
        for d in destinos:
            print(f"{d.nombre:<15} {self._pesos(d.precio_pasaje):<12} "
                  f"{self._pesos(d.precio_encomienda):<12}")

    def mostrar_vuelos(self, vuelos):
        print("=== VUELOS ===")
        print(f"{'Codigo':<8} {'Fecha':<12} {'Destino':<15} {'Hora':<6} "
              f"{'Avion':<20} {'Asientos':<9}")
        for v in vuelos:
            asientos = f"{v.asientos_libres()}/{v.avion.capacidad_pasajeros}"
            print(f"{v.codigo:<8} {str(v.fecha):<12} {v.destino.nombre:<15} {v.hora:<6} "
                  f"{v.avion.modelo:<20} {asientos:<9}")
