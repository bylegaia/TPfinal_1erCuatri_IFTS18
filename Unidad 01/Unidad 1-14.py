""" Define una clase Playlist que tenga una lista de canciones. Usa composición para representar la relación entre una lista de reproducción y las canciones que la componen. """

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
        # for cancion in lista_inicial:
        #     self.canciones.append(Cancion(**cancion))
    
    @property
    def mostrar_playlist(self):
        return self.canciones
    
    def agregar_cancion(self, nuevas_canciones):
        for cancion in nuevas_canciones:
            self.canciones.append(Cancion(**cancion))

    def __str__(self) -> str:
        return f"Lista de Reproduccion: {self.nombre}\nCantidad de canciones: {len(self.canciones)}"    

class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nArtista: {self.artista}\nDuracion: {self.duracion}"

cancion1 = {
    "nombre": "Countdown To Shutdown",
    "artista": "The Hives",
    "duracion": "3:14"
}

cancion2 = {
    "nombre": "New Born",
    "artista": "Muse",
    "duracion": "6:04"
}

cancion3 = {
    "nombre": "Snow (Hey Oh)",
    "artista": "Red Hot Chilli Pepper",
    "duracion": "5:35"
}

playlist1 = Playlist("Rock")

playlist1.agregar_cancion([cancion1, cancion2, cancion3])

print(playlist1)
for tema in playlist1.mostrar_playlist:
    print("-" * 30)
    print(tema)
print("-" * 30)