"""  Crea una clase base Vehiculo con atributos como marca, modelo y color. Luego, crea clases derivadas como Coche, Moto, etc., que hereden de Vehiculo y agreguen atributos y métodos específicos. """

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo 
        self.color = color

    def acelerar(self):
        pass

    def detener(self):
        pass

    def girar(self):
        pass

    def mostrar_info(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\n"
    
class Auto(Vehiculo):
    CANTIDAD_RUEDAS = 4
    def __init__(self, marca, modelo, color, cantidad_puertas = 3, tablero_digital = False):
        super().__init__(marca, modelo, color)
        self.cantida_puertas = cantidad_puertas
        self.tablero_digital = tablero_digital

    def acelerar(self):
        return f"Acelerando {self.modelo} {self.marca}"
    
    def detener(self):
        return f"Deteniendo {self.modelo} {self.marca}"
    
    def girar(self):
        return f"Girando {self.modelo} {self.marca}"
    
    def mostrar_info(self):
        tablero = "Digital" if self.tablero_digital == True else "Analogico"
        return f"{super().mostrar_info()} Cantidad de Puertas: {self.cantida_puertas}\n Cantidad de Ruedas: {self.CANTIDAD_RUEDAS}\n Tablero: {tablero}"
    
class Moto(Vehiculo):
    cantidad_ruedas = 2
    def __init__(self, marca, modelo, color, cabina_pasajero = False):
        super().__init__(marca, modelo, color)
        self.cabina_pasajero = cabina_pasajero

    def acelerar(self):
        return f"Acelerando {self.modelo} {self.marca}"
    
    def detener(self):
        return f"Deteniendo {self.modelo} {self.marca}"
    
    def girar(self):
        return f"Girando {self.modelo} {self.marca}"
    
    def mostrar_info(self):
        cabina = ""
        if self.cabina_pasajero == True:
            self.cantidad_ruedas = 3
            cabina = "\n Tiene cabina de pasajero"
        return f"{super().mostrar_info()} Cantidad de Ruedas: {self.cantidad_ruedas}{cabina}"

separar = "-" * 30
auto1 = Auto("DeLorean", "DMC-12", "Gris", 3, True)
auto2 = Auto("Chevrolet", "Camaro", "Amarillo")
moto1 = Moto("Kawasaki", "ZZR 250", "Amarillo")
moto2 = Moto("Dakota", "Stunt Cycle", "Blanco", True)

print(auto1.mostrar_info())
print(separar)
print(auto2.mostrar_info())
print(separar)
print(moto1.mostrar_info())
print(separar)
print(moto2.mostrar_info())
