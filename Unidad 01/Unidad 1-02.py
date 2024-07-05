""" Crea una clase Persona con atributos nombre y edad. Crea un método para imprimir los datos de la persona. """

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"
    
persona = Persona("Alejo", 28)

print(persona.mostrar_informacion())