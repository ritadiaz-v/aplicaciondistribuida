# prueba_conexion.py
import pymysql

try:
    conexion = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",  # Si no tienes contraseña, déjalo vacío
        database="agenda_citas"
    )
    print("Conexión exitosa con PyMySQL")
    conexion.close()

except pymysql.MySQLError as e:
    print(f" Error de conexión: {e}")
