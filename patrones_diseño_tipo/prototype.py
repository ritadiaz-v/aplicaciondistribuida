import copy
#clase citamedica con el metodo clonar
class CitaMedica:
    def __init__(self, paciente, especialidad, fecha):
        self.paciente = paciente
        self.especialidad = especialidad
        self.fecha = fecha
        self.observaciones = None
        self.receta = None
        self.videollamada = False

    def mostrar(self):
        print(f"Paciente: {self.paciente}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Fecha: {self.fecha}")
        print(f"Observaciones: {self.observaciones}")
        print(f"Receta: {self.receta}")
        print(f"Videollamada: {self.videollamada}")

    def clonar(self):
        return copy.deepcopy(self)
    #cliente que clona
if __name__ == "__main__":
    cita_original = CitaMedica("Juan Pérez", "Dermatología", "2025-06-20")
    cita_original.observaciones = "Paciente con alergias"
    cita_original.receta = "Antihistamínicos"
    cita_original.videollamada = True

    print("Cita original:")
    cita_original.mostrar()

    print("\n Cita clonada para otro paciente:")
    cita_clonada = cita_original.clonar()
    cita_clonada.paciente = "Ana Torres"
    cita_clonada.fecha = "2025-06-22"
    cita_clonada.mostrar()
