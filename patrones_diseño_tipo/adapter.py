# interfaz Notificador
class Notificador:
    def enviar(self, mensaje):
        print(f"Enviando mensaje: {mensaje}")
#interfaz diferente
class ServicioExternoSMS:
    def send_text(self, texto):
        print(f"[SMS EXTERNO] {texto}")
#adaptador
class AdaptadorSMS(Notificador):
    def __init__(self, servicio_sms):
        self.servicio_sms = servicio_sms

    def enviar(self, mensaje):
        self.servicio_sms.send_text(mensaje)
#cliente cita medica
class CitaMedica:
    def __init__(self, notificador):
        self.notificador = notificador

    def agendar(self):
        print("Cita médica agendada.")
        self.notificador.enviar("Recuerde su cita el lunes a las 9 AM")
#uso
if __name__ == "__main__":
    servicio_sms = ServicioExternoSMS()
    adaptador = AdaptadorSMS(servicio_sms)

    cita = CitaMedica(adaptador)
    cita.agendar()
