class ConexionDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Conectando a la base de datos...")
            cls._instancia = super().__new__(cls)
            cls._instancia.conectar()
        return cls._instancia

    def conectar(self):
        self.conexion = "Conexión establecida"
    
    def ejecutar_query(self, sql):
        print(f"Ejecutando: {sql}")
conn1 = ConexionDB()
conn2 = ConexionDB()
print(conn1 is conn2)  # True
conn1.ejecutar_query("SELECT * FROM citas")
