""" Crea una clase Usuario con atributos como nombre, email y contraseña. Crea métodos para cambiar la contraseña y para mostrar la información del usuario. """

class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    def mostrar_informacion(self) -> str:
        return f"Nombre: {self.nombre}\nEmail: {self.email}\nContraseña: {self.contraseña}"
    
    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña # plenamente se reemplaza la contraseña antigua por la nueva
        return self.contraseña
    
usuario1 = Usuario("Alejo", "alejo.elalle@hotmail.com", "asd123")

print(usuario1.mostrar_informacion())
usuario1.cambiar_contraseña("zxc789")
print(usuario1.mostrar_informacion())