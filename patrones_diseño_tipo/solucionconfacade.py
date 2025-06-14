#subsistemas
class VerificadorDisponibilidad:
    def verificar(self, fecha):
        print(f"Verificando disponibilidad para {fecha}")
        return True

class RegistroCita:
    def registrar(self, fecha, paciente):
        print(f"Cita registrada para {paciente} el {fecha}")

class NotificadorCorreo:
    def enviar(self, mensaje):
        print(f"[Correo] {mensaje}")

class Confirmador:
    def generar(self, paciente):
        print(f"Confirmación generada para {paciente}")
#fachada
class FachadaAgendaMedica:
    def __init__(self):
        self.verificador = VerificadorDisponibilidad()
        self.registro = RegistroCita()
        self.notificador = NotificadorCorreo()
        self.confirmador = Confirmador()

    def agendar_cita(self, fecha, paciente):
        if self.verificador.verificar(fecha):
            self.registro.registrar(fecha, paciente)
            self.notificador.enviar("Su cita ha sido registrada.")
            self.confirmador.generar(paciente)
        else:
            print("No hay disponibilidad.")
#cliente
if __name__ == "__main__":
    fachada = FachadaAgendaMedica()
    fachada.agendar_cita("2025-06-20", "Juan Pérez")
