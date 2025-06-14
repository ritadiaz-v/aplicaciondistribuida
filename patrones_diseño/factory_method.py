#Importamos ABC (Abstract Base Class) y abstractmethod del módulo abc, 
# que permiten definir clases y métodos abstractos
from abc import ABC, abstractmethod 

#Notificacion es clase abstracta que define el contrato que todas las notificaciones 
# deben seguir: tener un método enviar. 
# No se puede crear una instancia de Notificacion directamente

# Producto
class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass

# EmailNotificacion y SMSNotificacion Estas son las clases concretas que implementan el método enviar. 
# Cada una tiene su propia lógica para enviar la notificación.
# Productos concretos
class EmailNotificacion(Notificacion):
    def enviar(self):
        return "Enviando notificación por correo electrónico"

class SMSNotificacion(Notificacion):
    def enviar(self):
        return "Enviando notificación por SMS"

# Define el método factory crear_notificacion(), que debe devolver un objeto del tipo Notificacion.
# Esta clase es abstracta, no se puede instanciar directamente
# Creador
class NotificacionCreator(ABC):
    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        pass

# Estas clases concretas implementan el método crear_notificacion() devolviendo una instancia del producto correspondiente.
# Aquí está el verdadero uso del patrón Factory Method: cada subclase decide qué clase concreta instanciar
# Creadores concretos
class EmailCreator(NotificacionCreator):
    def crear_notificacion(self) -> Notificacion:
        return EmailNotificacion()

class SMSCreator(NotificacionCreator):
    def crear_notificacion(self) -> Notificacion:
        return SMSNotificacion()

# Esta función no sabe qué tipo de notificación va a enviar.
# Solo espera un objeto que implemente la interfaz NotificacionCreator, y llama al método enviar() del producto creado.
# Uso
def enviar_notificacion(creator: NotificacionCreator):
    notificacion = creator.crear_notificacion()
    print(notificacion.enviar())

enviar_notificacion(EmailCreator())  # Enviando notificación por correo electrónico
enviar_notificacion(SMSCreator())    # Enviando notificación por SMS
