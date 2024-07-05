""" Define una clase abstracta llamada Empleado que tenga métodos abstractos como calcular_sueldo() y generar_reporte(). Luego, crea clases concretas como Desarrollador, Gerente, Contador, etc., que hereden de Empleado y proporcionen implementaciones concretas para estos métodos. """

class Empleado():
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def calcular_sueldo(self):
        pass

    def generar_reporte(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado, nivel, salario_base):
        super().__init__(nombre, id_empleado)
        self.nivel = nivel
        self.salario_base = salario_base
        self.proyectos_asignados = []

    def asignar_proyecto(self, *proyectos):
        for proyecto in proyectos:
            self.proyectos_asignados.append(proyecto)
    
    def quitar_proyecto(self, *proyectos): 
        for proyecto in proyectos:
            if proyecto in self.proyectos_asignados:
                self.proyectos_asignados.remove(proyecto)

    def calcular_sueldo(self):
        extra_por_proyecto = 30000 * len(self.proyectos_asignados)
        return self.salario_base + extra_por_proyecto
        

    def generar_reporte(self):
        lista_proyecto = ""
        if len(self.proyectos_asignados) == 0:
            lista_proyecto = "No hay proyectos asignados"
        else:
            for numero, proyecto in enumerate(self.proyectos_asignados, 1):
                lista_proyecto += f" Proyecto {numero}: {proyecto}\n"
        return f"Desarrollador: {self.nombre}\nID: {self.id_empleado}\nSueldo: {self.calcular_sueldo()}\nProyectos asignados:\n{lista_proyecto}"

class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, equipo):
        super().__init__(nombre, id_empleado)
        self.salario_base = salario_base
        self.equipo = equipo
        # for empleado_asignado in empleados_a_cargo:
        #     self.equipo.append(**empleado_asignado)

    def calcular_sueldo(self):
        return self.salario_base + (50000 * len(self.equipo))

    def generar_reporte(self):
        lista_equipo = ""
        if len(self.equipo) == 0:
            lista_equipo = "No tiene empleados asignados"
        else:
            for empleado in self.equipo:
                lista_equipo += f" Empleado {empleado.id_empleado}: {empleado.nombre}\n"
        return f"Gerente: {self.nombre}\nID: {self.id_empleado}\nSueldo: {self.calcular_sueldo()}\nEquipo a cargo:\n{lista_equipo}"

class Contador(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, comision):
        super().__init__(nombre, id_empleado)
        self.salario_base = salario_base
        self.comision = comision

    def calcular_sueldo(self):
        return self.salario_base + self.comision

    def generar_reporte(self):
        return f"Contador: {self.nombre}\nID: {self.id_empleado}\nSueldo: {self.calcular_sueldo()}"


empleado1 = Desarrollador("Alejo", 1, "Trainee", 350000)
empleado1.asignar_proyecto("Proyecto A", "Proyecto C")
empleado2 = Desarrollador("Dante", 2, "Junior", 450000)
empleado2.asignar_proyecto("Proyecto A", "Proyecto B", "Proyecto C")
empleado3 = Desarrollador("Vergil", 3, "Senior", 600000)
empleado3.asignar_proyecto("Proyecto A")

equipo_a = [empleado1, empleado2, empleado3]

empleado4 = Gerente("Gwyn", 4, 600000, equipo_a)
empleado5 = Contador("Tony", 5, 400000, 10000)

empresa = equipo_a + [empleado4, empleado5]

for empleado in empresa:
    print("-" * 30)
    print(f"{empleado.generar_reporte()}")
print("-" * 30)