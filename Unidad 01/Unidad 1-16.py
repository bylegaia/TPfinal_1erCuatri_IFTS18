""" Implementa una clase Aula que tenga una lista de estudiantes y un profesor. Usa composición para representar la relación entre un aula y las personas que la ocupan. """

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}"
    
class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, asignatura):
        super().__init__(nombre, apellido, edad)
        self.asignatura = Asignatura(**asignatura)

    def __str__(self) -> str:
        return f"{super().__str__()}\n -Asignatura-\n{self.asignatura}"


class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self._contenidos = []

    @property
    def mostrar_contenidos(self) -> list:
        return self._contenidos
    
    def agregar_contenidos(self, tema):
        self._contenidos.append(**tema)

    def __str__(self) -> str:
        return self.nombre
    
class Alummno(Persona):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)

    def __str__(self) -> str:
        return f" -Alumno-\n{super().__str__()}"


class Aula:
    def __init__(self, numero, division, profesor, alumnos: list):
        self.numero = numero
        self.division = division
        self._profesor = Profesor(**profesor)
        self._alumnos = []
        for alumno in alumnos:
            self._alumnos.append(Alummno(**alumno))

    @property
    def mostrar_profesor(self):
        return self._profesor
    
    def reemplazar_profesor(self, nuevo_profesor):
        self._profesor = Profesor(**nuevo_profesor)
    
    @property
    def mostrar_alumnos(self):
        return self._alumnos
    
    def agregar_alumno(self, nuevo_alumno):
        self._alumnos.append(Alummno(**nuevo_alumno))

    def quitar_alumno(self, alumno_eliminado):
        for alumno in self._alumnos:
            if alumno_eliminado.get("nombre") == alumno.nombre and alumno_eliminado.get("apellido") == alumno.apellido:
                self._alumnos.remove(alumno)
                break
    
    def __str__(self) -> str:
        return f"Aula: {self.numero}{self.division}\n -Profesor Asignado-\n{self._profesor}\n Cantidad de Alumnos: {len(self.mostrar_alumnos)}"

asignatura = {
    "nombre": "Hechiceria"
}

profesor = {
    "nombre": "Saturo",
    "apellido": "Gojo",
    "edad": 30,
    "asignatura": asignatura
}

alumno1 = {
    "nombre": "Juji",
    "apellido": "Itadori",
    "edad": 16
}

alumno2 = {
    "nombre": "Nobara",
    "apellido": "Kugisaki",
    "edad": 16
}

alumno3 = {
    "nombre": "Megumi",
    "apellido": "Fushiguro",
    "edad": 16
}

aula_instanciada = Aula("1º", "B", profesor, [alumno1, alumno2])

print(aula_instanciada)

for alumno in aula_instanciada.mostrar_alumnos:
    print("-" * 30)
    print(alumno)
print("-" * 30)

aula_instanciada.agregar_alumno(alumno3)

for alumno in aula_instanciada.mostrar_alumnos:
    print("-" * 30)
    print(alumno)
print("-" * 30)

aula_instanciada.quitar_alumno(alumno1)
aula_instanciada.quitar_alumno(alumno2)
aula_instanciada.quitar_alumno(alumno3)

print(aula_instanciada)