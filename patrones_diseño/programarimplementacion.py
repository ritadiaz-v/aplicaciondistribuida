class NotificadorEmail:
    def enviar(self, mensaje):
        print(f"Enviando por correo: {mensaje}")

class Cita:
    def __init__(self):
        self.notificador = NotificadorEmail()  # DEPENDE directamente de una clase concreta

    def agendar(self):
        self.notificador.enviar("Tiene una cita mañana")
