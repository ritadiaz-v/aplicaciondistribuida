#producto
class CitaMedica:
    def __init__(self):
        self.paciente = None
        self.especialidad = None
        self.fecha = None
        self.observaciones = None
        self.receta = None
        self.notificacion = None
        self.videollamada = None

    def mostrar(self):
        print(f"Paciente: {self.paciente}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Fecha: {self.fecha}")
        if self.observaciones:
            print(f"Observaciones: {self.observaciones}")
        if self.receta:
            print(f"Receta: {self.receta}")
        if self.notificacion:
            print(f"Notificación: {self.notificacion}")
        if self.videollamada:
            print("Incluye video-consulta.")
# clase builder
class CitaMedicaBuilder:
    def __init__(self):
        self.cita = CitaMedica()

    def con_paciente(self, nombre):
        self.cita.paciente = nombre
        return self

    def con_especialidad(self, especialidad):
        self.cita.especialidad = especialidad
        return self

    def con_fecha(self, fecha):
        self.cita.fecha = fecha
        return self

    def con_observaciones(self, obs):
        self.cita.observaciones = obs
        return self

    def con_receta(self, receta):
        self.cita.receta = receta
        return self

    def con_notificacion(self, medio):
        self.cita.notificacion = medio
        return self

    def con_videollamada(self):
        self.cita.videollamada = True
        return self

    def build(self):
        return self.cita
#patron builder
if __name__ == "__main__":
    builder = CitaMedicaBuilder()
    cita = (
        builder
        .con_paciente("María Gómez")
        .con_especialidad("Cardiología")
        .con_fecha("2025-06-15 10:00")
        .con_observaciones("Ayuno de 8 horas")
        .con_videollamada()
        .build()
    )

    cita.mostrar()

