import tkinter as tk
from tkinter import ttk, messagebox
from controlador_cita import obtener_citas, agregar_cita, eliminar_cita, editar_cita

# Crear ventana principal
root = tk.Tk()
root.title("Agenda de Citas Médicas")
root.geometry("700x400")

# Variables de los campos
entry_nombre = tk.Entry(root)
entry_fecha = tk.Entry(root)
entry_hora = tk.Entry(root)
entry_motivo = tk.Entry(root)

# Variable oculta para el ID
id_seleccionado = tk.StringVar()

# Función para mostrar citas en la tabla
def mostrar_citas():
    for row in tree.get_children():
        tree.delete(row)
    for cita in obtener_citas():
        tree.insert("", tk.END, values=cita)

# Función para limpiar campos
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_motivo.delete(0, tk.END)
    id_seleccionado.set("")

# Función al seleccionar una fila de la tabla
def on_select(event):
    seleccion = tree.selection()
    if seleccion:
        item = tree.item(seleccion[0])
        cita = item['values']
        id_seleccionado.set(str(cita[0]))  # ← Guardar ID oculto
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, cita[1])
        entry_fecha.delete(0, tk.END)
        entry_fecha.insert(0, cita[2])
        entry_hora.delete(0, tk.END)
        entry_hora.insert(0, cita[3])
        entry_motivo.delete(0, tk.END)
        entry_motivo.insert(0, cita[4])

# Funciones CRUD
def insertar():
    agregar_cita(entry_nombre.get(), entry_fecha.get(), entry_hora.get(), entry_motivo.get())
    mostrar_citas()
    limpiar_campos()

def actualizar():
    if not id_seleccionado.get():
        messagebox.showwarning("Atención", "Selecciona una cita para editar.")
        return
    editar_cita(
        int(id_seleccionado.get()),
        entry_nombre.get(),
        entry_fecha.get(),
        entry_hora.get(),
        entry_motivo.get()
    )
    mostrar_citas()
    limpiar_campos()

def borrar():
    if not id_seleccionado.get():
        messagebox.showwarning("Atención", "Selecciona una cita para eliminar.")
        return
    eliminar_cita(int(id_seleccionado.get()))
    mostrar_citas()
    limpiar_campos()

# Etiquetas y campos
tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0)
entry_fecha.grid(row=1, column=1)

tk.Label(root, text="Hora (HH:MM):").grid(row=2, column=0)
entry_hora.grid(row=2, column=1)

tk.Label(root, text="Motivo:").grid(row=3, column=0)
entry_motivo.grid(row=3, column=1)

# Botones
tk.Button(root, text="Insertar", command=insertar).grid(row=4, column=0, pady=10)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=4, column=1)
tk.Button(root, text="Eliminar", command=borrar).grid(row=4, column=2)
tk.Button(root, text="Limpiar", command=limpiar_campos).grid(row=4, column=3)

# Tabla
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Fecha", "Hora", "Motivo"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Motivo", text="Motivo")
tree.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Evento al seleccionar fila
tree.bind("<<TreeviewSelect>>", on_select)

# Mostrar datos iniciales
mostrar_citas()

root.mainloop()

