class NotificadorEmail:
    def enviar(self, mensaje):
        print(f"[EMAIL] {mensaje}")

class CitaMedica:
    def __init__(self):
        self.notificador = NotificadorEmail()  # ACOPLADO a una implementación

    def agendar(self):
        print("Cita agendada.")
        self.notificador.enviar("Recuerde su cita mañana a las 10 a.m.")
