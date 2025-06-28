import pymysql

def obtener_conexion():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="agenda_citas"
    )

def insertar_cita(nombre, fecha, hora, motivo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO citas (nombre_paciente, fecha, hora, motivo) VALUES (%s, %s, %s, %s)",
                       (nombre, fecha, hora, motivo))
    conexion.commit()
    conexion.close()

def obtener_citas():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre_paciente, fecha, hora, motivo FROM citas")
        citas = cursor.fetchall()
    conexion.close()
    return citas

def eliminar_cita(id_cita):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM citas WHERE id = %s", (id_cita,))
    conexion.commit()
    conexion.close()

def actualizar_cita(id_cita, nombre, fecha, hora, motivo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE citas
            SET nombre_paciente=%s, fecha=%s, hora=%s, motivo=%s
            WHERE id=%s
        """, (nombre, fecha, hora, motivo, id_cita))
    conexion.commit()
    conexion.close()
