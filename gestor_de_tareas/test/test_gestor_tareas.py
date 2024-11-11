# tests/test_gestor_tareas.py
import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.assertIn("Tarea 1", self.gestor.obtener_tareas())

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.eliminar_tarea("Tarea 1")
        self.assertNotIn("Tarea 1", self.gestor.obtener_tareas())

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.marcar_completada("Tarea 1")
        self.assertIn("Tarea 1", self.gestor.obtener_tareas_completadas())

    def test_obtener_tareas_completadas(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        self.gestor.marcar_completada("Tarea 1")
        self.assertEqual(self.gestor.obtener_tareas_completadas(), ["Tarea 1"])

    def test_obtener_tareas_no_completadas(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        self.gestor.marcar_completada("Tarea 1")
        self.assertEqual(self.gestor.obtener_tareas(), ["Tarea 2"])

if __name__ == '__main__':
    unittest.main()
