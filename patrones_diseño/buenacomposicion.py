class Agenda:
    def agendar(self):
        print("Cita registrada")

class Notificador:
    def enviar(self, mensaje):
        print(f"Notificando: {mensaje}")

class AgendaConNotificacion:
    def __init__(self, agenda: Agenda, notificador: Notificador):
        self.agenda = agenda
        self.notificador = notificador

    def agendar(self):
        self.agenda.agendar()
        self.notificador.enviar("Recuerde su cita")
# uso
agenda_base = Agenda()
notificador = Notificador()
agenda_final = AgendaConNotificacion(agenda_base, notificador)
agenda_final.agendar()
