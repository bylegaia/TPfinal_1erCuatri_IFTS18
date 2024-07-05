""" Desarrolla un juego de simulación de vida donde los "seres" pueden ser plantas, animales, personas, etc. Cada ser debe tener atributos como energía, salud, edad, etc., y comportamientos específicos según su tipo. """

class SerVivo:
    def __init__(self, energia, salud, edad):
        self.energia = energia
        self.salud = salud
        self.edad = edad

    def envejecer(self):
        self.edad += 1
        self.energia -= 50
        self.salud -= 25
        return "Envejece 1 año"

    def alimentarse(self):
        pass

    def descansar(self):
        self.energia += 20
        self.salud += 5
        return "Descansa"

    def muerte(self):
        self.energia = 0
        self.salud = 0
        return "Muerte"

    def estado(self):
        return f"Energía: {self.energia}\nSalud: {self.salud}\nEdad: {self.edad} años"

class Planta(SerVivo):
    def alimentarse(self):
        self.energia += 15
        return "La planta hace la fotosintesis"

class Animal(SerVivo):
    def __init__(self, energia, salud, edad, dieta: bool):
        super().__init__(energia, salud, edad)
        establecer_dieta = "Carnivoro" if dieta == True else "Herbivoro"
        self.dieta = establecer_dieta

    def alimentarse(self):
        self.energia += 10
        return "El animal sale a cazar" if self.dieta == "Carnivoro" else "Se alimenta del suelo"

    def estado(self):
        return f"{super().estado()}\nDieta: {self.dieta}"

class Persona(SerVivo):
    def __init__(self, energia, salud, edad, nombre, dinero):
        super().__init__(energia, salud, edad)
        self.nombre = nombre
        self.dinero = dinero

    def alimentarse(self):
        self.energia += 5
        return f"{self.nombre} se pide un Rappi"

    def trabajar(self):
        self.energia -= 20
        self.salud -= 10
        self.dinero += 100
        return f"{self.nombre} trabaja; pierde energía y salud pero gana dinero"

    def estado(self):
        return f"Nombre: {self.nombre}\n{super().estado()}\nDinero: §{self.dinero}"
    
arbol = Planta(400, 5000, 80)
leon = Animal(200, 750, 12, True)
gil_laburante = Persona(135, 300, 28, "Alejo", 1400)

seres_vivos = [arbol, leon, gil_laburante]

for ser_vivo in seres_vivos:
    print("-" * 30)
    print(ser_vivo.estado())
    print(ser_vivo.envejecer())
    print(ser_vivo.alimentarse())
    print(ser_vivo.estado())
    print(ser_vivo.descansar())
    print(ser_vivo.estado())
print("-" * 30)
