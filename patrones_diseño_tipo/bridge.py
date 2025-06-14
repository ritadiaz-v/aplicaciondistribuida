#canal de notificacion
from abc import ABC, abstractmethod

class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje): pass
class NotificadorCorreo(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"[Correo] {mensaje}")

class NotificadorWhatsApp(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"[WhatsApp] {mensaje}")
#abstraccion
class Recordatorio:
    def __init__(self, canal: CanalNotificacion):
        self.canal = canal

    def enviar_recordatorio(self, mensaje):
        self.canal.enviar(mensaje)
#subclases de abstracción
class RecordatorioTexto(Recordatorio):
    def enviar(self):
        self.enviar_recordatorio("Recordatorio: tiene una cita mañana a las 10 AM.")

class RecordatorioEmergencia(Recordatorio):
    def enviar(self):
        self.enviar_recordatorio("⚠️ EMERGENCIA: Acuda al hospital más cercano.")
#cliente
if __name__ == "__main__":
    # Enviar recordatorio de texto por correo
    r1 = RecordatorioTexto(NotificadorCorreo())
    r1.enviar()

    # Enviar emergencia por WhatsApp
    r2 = RecordatorioEmergencia(NotificadorWhatsApp())
    r2.enviar()
