""" Crea una clase base llamada Animal con atributos como nombre y edad. Luego, define clases derivadas como Perro, Gato, etc., que agreguen atributos específicos y métodos relacionados con cada tipo de animal. """

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"

class Perro(Animal):
    def __init__(self, nombre, edad: int, largo_pelaje, color_pelaje, raza):
        super().__init__(nombre, edad)
        self.largo_pelaje = largo_pelaje
        self.color_pelaje = color_pelaje
        self.raza = raza

    def mostrar_informacion(self): # aplicamos polimorfismo para mostrar la informacion generica del animal y agregarle los detalles unicos de un perro
        return f"{super().mostrar_informacion()}\nRaza: {self.raza}\nLargo del Pelaje: {self.largo_pelaje}\nColor del Pelaje: {self.color_pelaje}" 
    
class Ave(Animal):
    def __init__(self, nombre, edad: int, color_plumaje, especie, puede_volar=True):
        super().__init__(nombre, edad)
        self.color_plumaje = color_plumaje
        self.especie = especie
        self.puede_volar = puede_volar

    def mostrar_informacion(self):
        if self.puede_volar:
            self.puede_volar = "Si"
        else:
            self.puede_volar = "No"
        return f"{super().mostrar_informacion()}\nEspecie: {self.especie}\nColor de Plumas: {self.color_plumaje}\nEs capas de volar? {self.puede_volar}"
    
perro1 = Perro("Perrete", 10, "Corto", "Marron", "Salchicha")

ave1 = Ave("Mordecai", 3, "Azul", "Arrendajo Azul")

print(perro1.mostrar_informacion())
print(ave1.mostrar_informacion())