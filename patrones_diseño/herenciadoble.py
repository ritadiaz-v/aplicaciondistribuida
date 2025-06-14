class A:
    def saludar(self):
        print("Hola desde A")

class B:
    def saludar(self):
        print("Hola desde B")

class C(A, B):  # herencia múltiple
    pass

obj = C()
obj.saludar()
