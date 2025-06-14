class TimestampMixin:
    def obtener_fecha(self):
        print("Fecha: 2025-06-11")

class Cita:
    def procesar(self):
        print("Cita procesada")

class CitaConFecha(Cita, TimestampMixin):
    pass

c = CitaConFecha()
c.procesar()
c.obtener_fecha()
