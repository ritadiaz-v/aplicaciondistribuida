#interfaz base
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje): pass
#implementacion concreta
class NotificadorBase(Notificador):
    def enviar(self, mensaje):
        print(f"[Notificación] {mensaje}")
#decorador base
class DecoradorNotificador(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    def enviar(self, mensaje):
        self._notificador.enviar(mensaje)
#decorador concretos
class DecoradorMayusculas(DecoradorNotificador):
    def enviar(self, mensaje):
        super().enviar(mensaje.upper())

class DecoradorAlerta(DecoradorNotificador):
    def enviar(self, mensaje):
        super().enviar(f"⚠️ {mensaje}")

class DecoradorExtra(DecoradorNotificador):
    def enviar(self, mensaje):
        super().enviar(f"{mensaje} (Por favor no olvide asistir)")
#cliente
if __name__ == "__main__":
    notificador = NotificadorBase()

    # Decoradores encadenados
    notificador_con_alerta = DecoradorAlerta(notificador)
    notificador_mayus = DecoradorMayusculas(notificador_con_alerta)
    notificador_final = DecoradorExtra(notificador_mayus)

    notificador_final.enviar("Tiene una cita mañana a las 8am")
