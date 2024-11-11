# src/logica/gestor_tareas.py
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

    def eliminar(self):
        self.descripcion = None


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def eliminar_tarea(self, descripcion):
        self.tareas = [tarea for tarea in self.tareas if tarea.descripcion != descripcion]

    def marcar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                tarea.completar()

    def obtener_tareas(self):
        return [tarea.descripcion for tarea in self.tareas if not tarea.completada]

    def obtener_tareas_completadas(self):
        return [tarea.descripcion for tarea in self.tareas if tarea.completada]
