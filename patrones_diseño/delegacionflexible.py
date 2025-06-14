
from abc import ABC, abstractmethod


# Producto:Cita
class Cita(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass



# Productos concretos
class CitaMedica(Cita):
    def mostrar_info(self):
        return "Cita médica general con el Dr. Acosta"

class CitaOdontologica(Cita):
    def mostrar_info(self):
        return "Cita odontológica con la Dra. Díaz"


# Creador (Factory Method)
class CreadorCita(ABC):
    @abstractmethod
    def crear_cita(self) -> Cita:
        pass



# Creadores concretos
class CreadorCitaMedica(CreadorCita):
    def crear_cita(self) -> Cita:
        return CitaMedica()

class CreadorCitaOdontologica(CreadorCita):
    def crear_cita(self) -> Cita:
        return CitaOdontologica()



# Uso del factory method
def agendar(creador: CreadorCita):
    cita = creador.crear_cita()
    print(cita.mostrar_info())



# ejecucion
agendar(CreadorCitaMedica())        # Salida: Cita médica general con el Dr. Acosta
agendar(CreadorCitaOdontologica())  # Salida: Cita odontológica con la Dra. Díaz