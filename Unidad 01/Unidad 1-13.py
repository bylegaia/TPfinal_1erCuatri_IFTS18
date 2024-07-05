""" Crea una clase abstracta llamada Vehiculo que tenga métodos abstractos como acelerar() y frenar(). Luego, crea clases concretas como Coche, Moto, Bicicleta, etc., que hereden de Vehiculo y proporcionen implementaciones concretas para estos métodos. """

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        pass

    def frenar(self):
        pass

class Auto(Vehiculo):
    CANTIDAD_RUEDAS = 4
    def __init__(self, marca, modelo, color, cantidad_puertas):
        super().__init__(marca, modelo, color)
        self.cantidad_puertas = cantidad_puertas

    def acelerar(self):
        return f"El auto {self.marca} {self.modelo} esta acelerando"
    
    def frenar(self):
        return f"El auto {self.marca} {self.modelo} esta frenando"
    
class Moto(Vehiculo):
    CANTIDAD_RUEDAS = 2
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo, color)

    def acelerar(self):
        return f"La moto {self.marca} {self.modelo} esta acelerando"

    def frenar(self):
        return f"La moto {self.marca} {self.modelo} esta frenando"
    
class Bicicleta(Vehiculo):
    CANTIDAD_RUEDAS = 2
    def __init__(self, marca, modelo, color, motor=True):
        super().__init__(marca, modelo, color)
        self.motor = motor

    def acelerar(self):
        return f"La bicicleta {self.marca} {self.modelo} esta pedaleando"
        
    def frenar(self):
        return f"La moto {self.marca} {self.modelo} esta frenando"
    