class A:
    def saludo(self):
        print("Hola desde A")

class B(A):
    def saludo(self):
        print("Hola desde B")

class C(A):
    def saludo(self):
        print("Hola desde C")

class D(B, C):
    pass

d = D()
d.saludo()
