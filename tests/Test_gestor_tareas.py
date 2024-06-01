import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
        self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

    def test_agregar_tarea_sin_titulo(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción")

    def test_ver_tareas(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        tareas = self.gestor.ver_tareas()
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0].titulo, "Tarea 1")
        self.assertEqual(tareas[0].descripcion, "Descripción de la tarea 1")

        class Tarea:
            def __init__(self, titulo, descripcion):
                self.titulo = titulo
                self.descripcion = descripcion
                self.completada = False

            def marcar_como_completada(self):
                self.completada = True

                class GestorTareas:
                    # Métodos anteriores

                    def marcar_tarea_como_completada(self, titulo):
                        for tarea in self.tareas:
                            if tarea.titulo == titulo:
                                tarea.marcar_como_completada()
                                return
                        raise ValueError("Tarea no encontrada")

                    class TestGestorTareas(unittest.TestCase):
                        # Métodos anteriores

                        def test_marcar_tarea_como_completada(self):
                            self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
                            self.gestor.marcar_tarea_como_completada("Tarea 1")
                            self.assertTrue(self.gestor.tareas[0].completada)

        class GestorTareas:
            # Métodos anteriores

            def eliminar_tarea(self, titulo):
                for tarea in self.tareas:
                    if tarea.titulo == titulo:
                        self.tareas.remove(tarea)
                        return
                raise ValueError("Tarea no encontrada")

        class TestGestorTareas(unittest.TestCase):
            # Métodos anteriores

            def test_eliminar_tarea(self):
                self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
                self.gestor.eliminar_tarea("Tarea 1")
                self.assertEqual(len(self.gestor.tareas), 0)