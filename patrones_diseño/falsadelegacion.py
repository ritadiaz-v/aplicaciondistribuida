class CitaMedica:
    def __init__(self):
        self.notificador = NotificadorWhatsApp()  # acoplamiento rígido

    def agendar(self):
        print("Cita médica agendada.")
        self.notificador.enviar("Recuerde su cita médica")
