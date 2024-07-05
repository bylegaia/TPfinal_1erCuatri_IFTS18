""" Define una clase Figura con métodos como calcular_area() y calcular_perimetro(). Luego, crea clases derivadas como Triangulo, Cuadrado, etc., que sobrescriban estos métodos para calcular el área y perímetro de cada figura """

import math

class Figura:
    def __init__(self) -> int:
        """ abstraccion para inicializar cada figura"""
        pass

    def calcular_area(self) -> int:
        """ abstraccion para calcular el area de cada figura """
        pass

    def calcular_perimetro(self) -> int:
        """ abstraccion para calcular el perimetro de cada figura """
        pass

    def mostrar_info(self):
        return f"Area: {self.calcular_area()}\n Perimetro: {self.calcular_perimetro()}"

class Circulo(Figura):
    PI = 3.1416 # constante para representar pi
    def __init__(self, radio: int):
        self.radio = radio

    def calcular_area(self) -> int:
        return self.PI * self.radio**2
    
    def calcular_perimetro(self) -> int:
        return 2 * self.PI * self.radio
    
    def mostrar_info(self):
        return f"Circulo\n Radio: {self.radio}\n {super().mostrar_info()}"
    
class Cuadrado(Figura):
    def __init__(self, lados: int):
        self.lados = lados

    def calcular_area(self):
        return self.lados * self.lados
    
    def calcular_perimetro(self):
        return 4 * self.lados
    
    def mostrar_info(self):
        return f"Cuadrado\n Longitud de los lados: {self.lados}\n {super().mostrar_info()}"
    
class Triangulo(Figura):
    def __init__(self, lados: int, base: int):
        self.lados = lados
        self.base = base

    def calcular_area(self) -> int:
        altura = math.sqrt(self.lados**2 - (self.base/2)**2) # formula para calcular la altura del triangulo, math.sqrt es la funcion para usar una raiz cuadrada
        return (self.base * altura) / 2
    
    def calcular_perimetro(self) -> int:
        return self.lados + self.lados + self.base
    
    def mostrar_info(self):
        return f"Triangulo\n Longitud de ambos lados: {self.lados}\n Base: {self.base}\n {super().mostrar_info()}"
    
forma1 = Circulo(5)
forma2 = Cuadrado(8)
forma3 = Triangulo(6, 3)

lista_figuras = [forma1, forma2, forma3] # Guardo los objetos en una lista 

for figura in lista_figuras:
    """ recorro la lista de objetos para mostrar la informacion de cada uno en orden """
    print("-" * 30)
    print(figura.mostrar_info())
print("-" * 30)
    