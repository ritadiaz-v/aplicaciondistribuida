class Agenda:
    def agendar(self):
        print("Cita registrada")

class AgendaConNotificacion(Agenda):
    def agendar(self):
        super().agendar()
        print("Enviando notificación...")  # notificación fija
