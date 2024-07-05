"""  Crea un sistema de gestión de tareas que permita a los usuarios agregar, eliminar y actualizar tareas. Debe haber clases como Tarea, ListaTareas, etc. """

class Tarea:
    def __init__(self, titulo, contenido, hora_recordatorio):
        self.titulo = titulo
        self.contenido = contenido
        self.hora_recordatorio = hora_recordatorio
        self.completada = False

    def completar_tarea(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.titulo}:\n {self.contenido} - {estado} con recordatorio para las {self.hora_recordatorio}hs"


class ListaTareas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.tareas = []

    @property
    def mostrar_tareas(self):
        return self.tareas

    def agregar_tarea(self, tarea_nueva):
        self.tareas.append(Tarea(**tarea_nueva))

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)

    def actualizar_tarea(self, titulo, nuevo_titulo = None, nuevo_contenido = None, nueva_hora = None):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                if nuevo_titulo:
                    tarea.titulo = nuevo_titulo
                if nuevo_contenido:
                    tarea.contenido = nuevo_contenido
                if nueva_hora:
                    tarea.hora_recordatorio = nueva_hora
    
    def marcar_tarea_completada(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completar_tarea()

    def __str__(self) -> str:
        return f"Lista de Tareas de {self.usuario}\n Cantidad de tareas: {len(self.tareas)}"

tarea1 = {
    "titulo": "Comprar alimento de gato",
    "contenido": "Acordate comprar marca Excellent",
    "hora_recordatorio": "17:30"
}

tarea2 = {
    "titulo": "Continuar TP de Programacion",
    "contenido": "No te colgues salame",
    "hora_recordatorio": "15:30"
}

tarea3 = {
    "titulo": "Limpiar el baño",
    "contenido": "",
    "hora_recordatorio": "11:00"
}

mistareas = ListaTareas("Alejo")

mistareas.agregar_tarea(tarea1)
mistareas.agregar_tarea(tarea2)
mistareas.agregar_tarea(tarea3)

for tarea in mistareas.mostrar_tareas:
    print("-" * 30)
    print(tarea)
print("-" * 30)

mistareas.marcar_tarea_completada("Continuar TP de Programacion")

for tarea in mistareas.mostrar_tareas:
    print("-" * 30)
    print(tarea)
print("-" * 30)