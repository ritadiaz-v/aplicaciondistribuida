# acceso concurrente

import pymysql
import threading
import time

# Conexión a MySQL
def conectar():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='clinica',
        autocommit=False
    )

# Función que intenta reservar una cita
def reservar_cita(paciente, medico_id, fecha):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            print(f"{paciente} intentando reservar...")

            # Inicia transacción
            cursor.execute("START TRANSACTION;")

            # Bloquea la hora específica para ese médico
            cursor.execute("""
                SELECT * FROM citas 
                WHERE medico_id = %s AND fecha = %s 
                FOR UPDATE;   # bloquea la fila (si existe) para que ningun otro proceso modifique mientras dura esta transaccion
            """, (medico_id, fecha))

            resultado = cursor.fetchone()  #guarda el resultado de la consulta anterior
            
            if resultado:
                print(f"{paciente}: Ya está reservada la cita.")
                conn.rollback()  # cancela la transaccion por que no se puede insertar una cita duplicada
            else:
                # Simulamos tiempo de espera para provocar una colisión
                time.sleep(2)
                cursor.execute("""
                    INSERT INTO citas (paciente, medico_id, fecha)
                    VALUES (%s, %s, %s);
                """, (paciente, medico_id, fecha))
                conn.commit()
                print(f"{paciente}: ¡Cita reservada exitosamente!")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()  # Si hubo un error inesperado, deshacer todo
    finally:
        conn.close()

# Simular dos usuarios concurrentes
fecha_cita = '2025-06-21 10:00:00'
medico_id = 1

t1 = threading.Thread(target=reservar_cita, args=("Paciente A", medico_id, fecha_cita))
t2 = threading.Thread(target=reservar_cita, args=("Paciente B", medico_id, fecha_cita))

t1.start()
t2.start()

t1.join()
t2.join()
