from modelodatos_cita import insertar_cita, obtener_citas, eliminar_cita, actualizar_cita

def agregar_cita(nombre, fecha, hora, motivo):
    insertar_cita(nombre, fecha, hora, motivo)

def listar_citas():
    return obtener_citas()

def borrar_cita(id_cita):
    eliminar_cita(id_cita)

def editar_cita(id_cita, nombre, fecha, hora, motivo):
    actualizar_cita(id_cita, nombre, fecha, hora, motivo)
