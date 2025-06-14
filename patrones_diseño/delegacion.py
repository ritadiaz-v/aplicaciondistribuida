class Impresora:
    def imprimir(self, texto):
        print(f"Imprimiendo: {texto}")

class Documento:
    def __init__(self):
        self.impresora = Impresora()  # Delegación

    def imprimir_documento(self, texto):
        # En vez de imprimir directamente, delega la acción
        self.impresora.imprimir(texto)

# Uso
doc = Documento()
doc.imprimir_documento("Hola delegación!")

# La clase Documento no se encarga directamente de imprimir.
# En su lugar, tiene una instancia de Impresora y le delega esa responsabilidad.