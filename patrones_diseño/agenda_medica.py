# Se importan herramientas para crear interfaces abstractas, 
# que permiten definir clases y métodos 
# que deben ser implementados en clases derivadas
from abc import ABC, abstractmethod
# Esta es la interfaz común para todas las citas (el "producto").
# Define el método mostrar_info() que todas las citas deben implementar.
# Esta clase no se puede instanciar directamente.

# Producto:Cita
class Cita(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# CitaMedica y CitaOdontologica son implementaciones concretas del producto Cita.
# Cada una sobreescribe el método mostrar_info() 
# para ofrecer información personalizada.

# Productos concretos
class CitaMedica(Cita):
    def mostrar_info(self):
        return "Cita médica general con el Dr. Ramírez"

class CitaOdontologica(Cita):
    def mostrar_info(self):
        return "Cita odontológica con la Dra. González"

# Define el método factory abstracto crear_cita().
# Obliga a las subclases a decir qué tipo de cita concreta 
# se va a crear.

# Creador (Factory Method)
class CreadorCita(ABC):
    @abstractmethod
    def crear_cita(self) -> Cita:
        pass

# Cada clase concreta de creador define cómo crear una instancia del producto concreto.
# Aquí se ve el corazón del patrón Factory Method: el método crear_cita() 
# instancia productos concretos pero el código cliente no sabe qué tipo específico es.

# Creadores concretos
class CreadorCitaMedica(CreadorCita):
    def crear_cita(self) -> Cita:
        return CitaMedica()

class CreadorCitaOdontologica(CreadorCita):
    def crear_cita(self) -> Cita:
        return CitaOdontologica()

# Esta función no sabe ni le importa qué tipo de cita va a recibir.
# Solo espera un objeto que implemente el creador abstracto 
# (CreadorCita), y lo usa.

# Uso del factory method
def agendar(creador: CreadorCita):
    cita = creador.crear_cita()
    print(cita.mostrar_info())

# Se crean instancias de los creadores concretos y se pasan a la función agendar.
# Se genera el objeto correcto y se ejecuta su método mostrar_info().

# ejecucion
agendar(CreadorCitaMedica())        # Salida: Cita médica general con el Dr. Ramírez
agendar(CreadorCitaOdontologica())  # Salida: Cita odontológica con la Dra. González
