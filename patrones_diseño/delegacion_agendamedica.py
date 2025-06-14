class Notificador:
    def enviar_notificacion(self, mensaje):
        print(f"Notificación enviada: {mensaje}")

class CitaMedica:
    def __init__(self):
        self.notificador = Notificador()  # delegación

    def agendar(self):
        print("Cita médica agendada.")
        self.notificador.enviar_notificacion("Recuerde su cita médica mañana a las 10 a.m.")
#uso
cita = CitaMedica()
cita.agendar()
