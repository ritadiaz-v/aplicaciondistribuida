from abc import ABC, abstractmethod

# Producto
class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass

# Productos concretos
class EmailNotificacion(Notificacion):
    def enviar(self):
        return "Enviando notificación por correo electrónico"

class SMSNotificacion(Notificacion):
    def enviar(self):
        return "Enviando notificación por SMS"

# Creador
class NotificacionCreator(ABC):
    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        pass

# Creadores concretos
class EmailCreator(NotificacionCreator):
    def crear_notificacion(self) -> Notificacion:
        return EmailNotificacion()

class SMSCreator(NotificacionCreator):
    def crear_notificacion(self) -> Notificacion:
        return SMSNotificacion()

# Uso
def enviar_notificacion(creator: NotificacionCreator):
    notificacion = creator.crear_notificacion()
    print(notificacion.enviar())

enviar_notificacion(EmailCreator())  # Enviando notificación por correo electrónico
enviar_notificacion(SMSCreator())    # Enviando notificación por SMS
