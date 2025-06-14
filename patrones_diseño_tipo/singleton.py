class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando nueva instancia...")
            cls._instancia = super().__new__(cls)
        else:
            print("Reutilizando instancia existente.")
        return cls._instancia
a = Singleton()
b = Singleton()
print(a is b)  # True: ambos son la misma instancia
