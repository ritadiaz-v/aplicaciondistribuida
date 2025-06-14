class A:
    def accion(self):
        print("Acción en A")

class B:
    def accion(self):
        print("Acción en B")

class C(A, B):
    pass

c = C()
c.accion()  # Ambigüedad: ¿A o B?
