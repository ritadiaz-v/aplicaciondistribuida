from abc import ABC, abstractmethod

# INTERFAZ
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# IMPLEMENTACIONES
class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"Correo: {mensaje}")

class NotificadorWhatsApp(Notificador):
    def enviar(self, mensaje):
        print(f"WhatsApp: {mensaje}")

# USO GENÉRICO: NO conoce la implementación
class Cita:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def agendar(self):
        print("Cita agendada")
        self.notificador.enviar("Tiene una cita mañana")
# inyección de la implementación concreta:
cita1 = Cita(NotificadorEmail())
cita1.agendar()

cita2 = Cita(NotificadorWhatsApp())
cita2.agendar()
