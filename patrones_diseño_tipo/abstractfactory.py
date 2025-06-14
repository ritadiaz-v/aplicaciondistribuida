from abc import ABC, abstractmethod

# Productos abstractos
class NotificadorCorreo(ABC):
    @abstractmethod
    def enviar(self, mensaje): pass

class NotificadorSMS(ABC):
    @abstractmethod
    def enviar(self, mensaje): pass

# Implementaciones concretas
class CorreoReal(NotificadorCorreo):
    def enviar(self, mensaje):
        print(f"[Correo REAL] {mensaje}")

class SMSReal(NotificadorSMS):
    def enviar(self, mensaje):
        print(f"[SMS REAL] {mensaje}")

# Fábrica abstracta
class FabricaNotificadores(ABC):
    @abstractmethod
    def crear_correo(self): pass

    @abstractmethod
    def crear_sms(self): pass

# Fábrica concreta
class FabricaProduccion(FabricaNotificadores):
    def crear_correo(self):
        return CorreoReal()

    def crear_sms(self):
        return SMSReal()

# Cliente
class CitaMedica:
    def __init__(self, fabrica: FabricaNotificadores):
        self.notificador_correo = fabrica.crear_correo()
        self.notificador_sms = fabrica.crear_sms()

    def agendar(self):
        print("🩺 Cita médica agendada.")
        self.notificador_correo.enviar("Su cita es mañana a las 10 a.m.")
        self.notificador_sms.enviar("Recordatorio: cita médica programada.")

# Punto de entrada
if __name__ == "__main__":
    fabrica = FabricaProduccion()
    cita = CitaMedica(fabrica)
    cita.agendar()
