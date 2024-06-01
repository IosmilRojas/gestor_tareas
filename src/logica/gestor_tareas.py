class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def test_marcar_tarea_como_completada(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.marcar_tarea_como_completada("Tarea 1")
        self.assertTrue(self.gestor.tareas[0].completada)