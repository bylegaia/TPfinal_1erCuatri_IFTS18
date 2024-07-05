""" Crea una clase Cancion que tenga atributos como nombre, artista y duracion. Crea métodos para reproducir la canción y para mostrar sus detalles. """

class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def reproducir(self):
        return f"Reproduciendo {self.nombre} por {self.artista}"
    
    def detener(self):
        return f"Deteniendo {self.nombre} por {self.artista}"
    
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}\nArtista: {self.artista}\nDuracion: {self.duracion}"
    
cancion1 = Cancion("Hootsforce", "Gloryhammer", "3:51")

print(cancion1.reproducir())
print(cancion1.mostrar_informacion())
print(cancion1.detener())