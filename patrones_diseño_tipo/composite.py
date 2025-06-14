#componente base
from abc import ABC, abstractmethod

class Tarea(ABC):
    @abstractmethod
    def ejecutar(self): pass
#tarea simple
class TareaSimple(Tarea):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        print(f"Ejecutando tarea: {self.nombre}")
#tarea compuesta
class TareaCompuesta(Tarea):
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar(self, tarea: Tarea):
        self.tareas.append(tarea)

    def ejecutar(self):
        print(f"== Ejecutando conjunto: {self.nombre} ==")
        for tarea in self.tareas:
            tarea.ejecutar()
#cliente
if __name__ == "__main__":
    # Crear tareas simples
    confirmar = TareaSimple("Confirmar cita")
    notificar = TareaSimple("Enviar notificación")
    generar_ticket = TareaSimple("Generar ticket")

    # Crear tarea compuesta
    proceso_agenda = TareaCompuesta("Proceso de agendamiento")
    proceso_agenda.agregar(confirmar)
    proceso_agenda.agregar(notificar)
    proceso_agenda.agregar(generar_ticket)

    # Ejecutar todo
    proceso_agenda.ejecutar()

