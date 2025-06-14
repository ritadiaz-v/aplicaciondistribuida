class Impresora:
    def imprimir(self):
        print("Imprimiendo documento")

class Cita:
    def __init__(self):
        self.impresora = Impresora()

    def procesar(self):
        print("Procesando cita")
        self.impresora.imprimir()  # delegación/composición
