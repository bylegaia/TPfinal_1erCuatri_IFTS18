""" Crea una clase Empleado con atributos como nombre, salario y departamento. Crea clases derivadas como Desarrollador, Diseñador, etc., que añadan atributos y métodos propios de cada tipo de empleado. """

class Empleado:
    """ Clase base para formar a partir de esta, otras clases de otros puestos """
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def calcular_salario(self):
        """ Metodo para guardar el salario, al aplicar polimorfismo en otras clases se podra modificar segun el puesto """
        return self.salario

    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nSalario: {self.calcular_salario()}\nDepartamento: {self.departamento}\n" # Se muestra de forma ordenada los distintos atributos de la clase

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, nivel):
        super().__init__(nombre, salario, departamento)
        self.nivel = nivel
        self.proyectos_asignados = [] # Lista para guardar los proyectos en los que esta involucrado el empleado

    def asignar_proyecto(self, *proyectos):
        """ Metodo para agregar proyectos al empleado """
        for proyecto in proyectos:
            self.proyectos_asignados.append(proyecto)
    
    def quitar_proyecto(self, *proyectos): 
        """ Metodo para quitar proyectos al empleado """
        for proyecto in proyectos:
            if proyecto in self.proyectos_asignados:
                self.proyectos_asignados.remove(proyecto)

    def calcular_salario(self):
        """ Se trae de la clase base, el sueldo cambia segun la cantidad de proyectos que el empleado este trabajando al mismo tiempo """
        extra_por_proyecto = 100000 * len(self.proyectos_asignados)
        salario_final = self.salario + extra_por_proyecto
        return salario_final
    
    def mostrar_info(self):
        """ Se trae de la clase base, se agrega una lista de los proyectos asignados ademas de su antiguedad en la empresa """
        lista_proyecto = ""
        if len(self.proyectos_asignados) == 0: # en caso de que no tenga ningun proyecto en el momento, se llama al mensaje correspondiente
            lista_proyecto = "No hay proyectos asignados"
        else:
            for numero, proyecto in enumerate(self.proyectos_asignados, 1):
                lista_proyecto += f"Proyecto {numero}: {proyecto}\n"
        return f"{super().mostrar_info()}Experiencia: {self.nivel}\n{lista_proyecto}"
    
separar = "-" * 30

empleado1 = Desarrollador("Alejo", 400000, "Desarrollo Backend", "Trainee")

empleado1.asignar_proyecto("Proyecto A", "Proyecto B")

print(empleado1.mostrar_info())

print(separar)

empleado1.quitar_proyecto("Proyecto A")

print(empleado1.mostrar_info())