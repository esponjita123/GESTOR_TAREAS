# src/vista/gui_gestor_tareas.py
import tkinter as tk
from tkinter import messagebox
from src.logica.gestor_tareas import GestorTareas

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Definir tamaño de la ventana
        self.root.geometry("600x400")  # Ancho x Alto
        self.root.resizable(True, True)  # Permitir que el usuario cambie el tamaño

        # Centrar la ventana en la pantalla
        self.center_window(600, 400)  # Ancho y Alto de la ventana

        # Colores
        self.root.configure(bg='#f0f0f0')  # Color de fondo de la ventana

        # Crear la instancia de GestorTareas
        self.gestor_tareas = GestorTareas()

        # Crear los widgets
        self.crear_widgets()

    def center_window(self, width, height):
        # Obtiene el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)

        # Establece la geometría de la ventana en base a los cálculos anteriores
        self.root.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def crear_widgets(self):
        # Caja de entrada para la tarea
        self.entry_tarea = tk.Entry(self.root, width=40, font=('Arial', 14), bd=2, relief="solid")
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botón para agregar tarea
        self.btn_agregar = tk.Button(self.root, text="Agregar Tarea", command=self.agregar_tarea,
                                      font=('Arial', 12), bg='#4CAF50', fg='white', relief="raised")
        self.btn_agregar.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.root, width=50, height=15, font=('Arial', 12), bd=2, relief="sunken", bg="#ffffff")
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botones para marcar como completada y eliminar
        self.btn_completar = tk.Button(self.root, text="Completar Tarea", command=self.completar_tarea,
                                       font=('Arial', 12), bg='#2196F3', fg='white', relief="raised")
        self.btn_completar.grid(row=2, column=0, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea,
                                      font=('Arial', 12), bg='#f44336', fg='white', relief="raised")
        self.btn_eliminar.grid(row=2, column=1, padx=10, pady=10)

        # Actualizar la lista de tareas
        self.actualizar_lista()

    def agregar_tarea(self):
        descripcion = self.entry_tarea.get()
        if descripcion:
            self.gestor_tareas.agregar_tarea(descripcion)
            self.entry_tarea.delete(0, tk.END)
            self.actualizar_lista()

    def completar_tarea(self):
        tarea_seleccionada = self.lista_tareas.get(tk.ACTIVE)
        if tarea_seleccionada:
            self.gestor_tareas.marcar_completada(tarea_seleccionada)
            self.actualizar_lista()

    def eliminar_tarea(self):
        tarea_seleccionada = self.lista_tareas.get(tk.ACTIVE)
        if tarea_seleccionada:
            self.gestor_tareas.eliminar_tarea(tarea_seleccionada)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        tareas = self.gestor_tareas.obtener_tareas()
        for tarea in tareas:
            self.lista_tareas.insert(tk.END, tarea)

# Función para iniciar la ventana principal
def iniciar_ventana():
    root = tk.Tk()  # Crear la ventana principal de Tkinter
    app = App(root)  # Crear la aplicación
    root.mainloop()  # Iniciar el bucle de eventos de Tkinter

if __name__ == "__main__":
    iniciar_ventana()  # Llamar a la función que inicia la ventana
