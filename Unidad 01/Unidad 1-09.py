""" Crea una función reproducir() que acepte cualquier objeto que represente un medio de entretenimiento (como una canción, película, libro, etc.) y lo reproduzca. """

class Multimedia:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def mostrar_info(self):
        return f" Nombre: {self.nombre}\n Duracion: {self.duracion}"
    
class Musica(Multimedia):
    def __init__(self, nombre, duracion, artista):
        super().__init__(nombre, duracion)
        self.artista = artista

    def mostrar_info(self):
        return f"{super().mostrar_info()}\n Artista: {self.artista}"
    
class Pelicula(Multimedia):
    def __init__(self, nombre, duracion, director):
        super().__init__(nombre, duracion)
        self.director = director

    def mostrar_info(self):
        return f"{super().mostrar_info()}\n Director: {self.director}"
    
class Audiolibro(Multimedia):
    def __init__(self, nombre, duracion, autor):
        super().__init__(nombre, duracion)
        self.autor = autor
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\n Autor: {self.autor}"
    
multimedia1 = Musica("Humming The Bassline", "2:55", "Hideki Naganuma")
multimedia2 = Pelicula("Hot Fuzz", "2h 1m", "Edgar Wright")
multimedia3 = Audiolibro("Mistborn", "24h 39m", "Brandon Sanderson")

lista_reproduccion = [multimedia1, multimedia2, "Libro fisico", multimedia3]

def reproductor(multimedia):
    if isinstance(multimedia, Multimedia): # isinstance comprueba que el objeto que pase por el reproductor se haya instanciado de la clase Multimedia
        print(f" - Reproduciendo -\n{multimedia.mostrar_info()}")
    else:
        print("Archivo incompatible")

for objeto in lista_reproduccion:
    print("-" * 30)
    reproductor(objeto)
print("-" * 30)