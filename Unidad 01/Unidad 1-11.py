""" Crea una clase abstracta llamada Animal que tenga métodos abstractos como hacer_sonido() y moverse(). Luego, crea clases concretas como Perro, Gato, Pájaro, etc., que hereden de Animal y proporcionen implementaciones concretas para estos métodos. """

class Animal:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def hacer_sonido(self):
        pass

    def moverse(self):
        pass

    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nColor: {self.color}"
    
class Perro(Animal):
    def __init__(self, nombre, edad, color, tipo_pelaje, raza):
        super().__init__(nombre, edad, color)
        self.tipo_pelaje = tipo_pelaje
        self.raza = raza

    def hacer_sonido(self):
        return f"{self.nombre} esta ladrando"
    
    def moverse(self):
        return f"{self.nombre} camina"
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTipo de pelaje: {self.tipo_pelaje}\nRaza: {self.raza}"
    
class Gato(Animal):
    def __init__(self, nombre, edad, color, tipo_pelaje, raza):
        super().__init__(nombre, edad, color)
        self.tipo_pelaje = tipo_pelaje
        self.raza = raza

    def hacer_sonido(self):
        return f"{self.nombre} esta maullando"
    
    def moverse(self):
        return f"{self.nombre} camina"
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\nTipo de pelaje: {self.tipo_pelaje}\nRaza: {self.raza}"

class Pajaro(Animal):
    def __init__(self, nombre, edad, color, tipo_plumaje, capacidad_volar = True):
        super().__init__(nombre, edad, color)
        self.tipo_plumaje = tipo_plumaje
        self.capacidad_volar = capacidad_volar

    def hacer_sonido(self):
        return f"{self.nombre} esta cantando"
    
    def moverse(self):
        return f"{self.nombre} vuela" if self.capacidad_volar == True else f"{self.nombre} camina"
    
    def mostrar_info(self):
        vuela = f"Puede volar" if self.capacidad_volar == True else f"No puede volar"
        return f"{super().mostrar_info()}\nTipo de Pelaje: {self.tipo_plumaje}\n{vuela}"
    

animal1 = Perro("Ayudante de Santa", 5, "Marron", "Corto", "Galgo Ingles")
animal2 = Gato("Bola de Nieve II", 3, "Negro", "Corto", "Gato Americano")
animal3 = Pajaro("ya me quede sin ideas xd", 7, "Marron", "Largo", capacidad_volar=False)

zoo = [animal1, animal2, animal3]

for animal in zoo:
    print("-" * 30)
    print(f"{animal.hacer_sonido()}")
    print("-" * 30)
    print(f"{animal.mostrar_info()}")
print("-" * 30)
