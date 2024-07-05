"""  Desarrolla un simulador de una ciudad donde puedas controlar aspectos como la población, la economía, la seguridad, etc. Crea clases como Ciudadano, Edificio, Vehículo, etc """

class Ciudadano:
    def __init__(self, nombre, edad, dinero, trabajo = None):
        self.nombre = nombre
        self.edad = edad
        self.trabajo = Trabajo(**trabajo)
        self.salud = 100
        self.dinero = dinero

    def conseguir_trabajo(self, trabajo_nuevo):
        self.trabajo = Trabajo(**trabajo_nuevo)

    def renunciar_trabajo(self):
        self.trabajo = None if self.trabajo != None else self.trabajo

    def trabajar(self):
        self.salud -= 1
        self.dinero += self.trabajo.obtener_ganancia

    @property
    def mostrar_ciudadano(self) -> str:
        tiene_trabajo = f"\nTrabajo:\n{self.trabajo}" if self.trabajo != None else ""
        return f"Nombre: {self.nombre}\nEdad: {self.edad} años\nSalud: {self.salud}%{tiene_trabajo}\nDinero: ${self.dinero}"

    def __str__(self) -> str:
        return self.nombre

class Trabajo:
    def __init__(self, empresa, puesto, ganancia):
        self.empresa = Empresa(**empresa)
        self.puesto = puesto
        self._ganancia = ganancia

    @property
    def obtener_ganancia(self):
        return self._ganancia

    def __str__(self) -> str:
        return f" Puesto: {self.puesto}\n Sueldo por dia: ${self._ganancia}\n Empresa: {self.empresa.nombre}"

class Empresa:
    def __init__(self, nombre, edificio):
        self.nombre = nombre
        self.edificio = Edificio(**edificio)

    def __str__(self) -> str:
        return f"Empresa: {self.nombre}\n {self.edificio}"

class Edificio:
    def __init__(self, tipo, pisos, direccion):
        self.tipo = tipo
        self.pisos = pisos
        self.direccion = direccion

    def __str__(self) -> str:
        return f"Edificio: {self.tipo}\nCantidad de Pisos: {self.pisos}\nUbicacion: {self.direccion}"

class Vehiculo:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def __str__(self) -> str:
        return f"Vehículo: {self.modelo} {self.marca}"


class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudadanos = []
        self.edificios = []
        self.vehiculos = []

    def agregar_ciudadano(self, ciudadano):
        self.ciudadanos.append(ciudadano)

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self) -> str:
        return self.nombre



""" Le pedi a chatgpt ideas de como instanciar y probar todo lo que escribi antes, sorry about that """
""" Y aun asi le tuve que corregir cosas xd """



# Crear instancias de Edificio
edificio1 = Edificio(tipo="Residencial", pisos=10, direccion="Calle Principal 123")
edificio2 = Edificio(tipo="Comercial", pisos=5, direccion="Avenida Secundaria 456")

# Crear instancias de Empresa
empresa1 = {"nombre": "TechCorp", "edificio": {"tipo": "Oficinas", "pisos": 15, "direccion": "Boulevard Empresarial 789"}}
empresa2 = {"nombre": "HealthInc", "edificio": {"tipo": "Hospital", "pisos": 8, "direccion": "Calle Salud 101"}}

# Crear instancias de Trabajo
trabajo1 = {"empresa": empresa1, "puesto": "Ingeniero", "ganancia": 5000}
trabajo2 = {"empresa": empresa2, "puesto": "Doctor", "ganancia": 6000}

# Crear instancias de Ciudadano
ciudadano1 = Ciudadano(nombre="Juan", edad=30, dinero=1000, trabajo=trabajo1)
ciudadano2 = Ciudadano(nombre="Maria", edad=28, dinero=2000, trabajo=trabajo2)

# Crear instancias de Vehiculo
vehiculo1 = Vehiculo(modelo="Sedan", marca="Toyota")
vehiculo2 = Vehiculo(modelo="SUV", marca="Honda")

# Crear una instancia de Ciudad y agregar elementos
ciudad = Ciudad(nombre="Metropolis")
ciudad.agregar_ciudadano(ciudadano1)
ciudad.agregar_ciudadano(ciudadano2)
ciudad.agregar_edificio(edificio1)
ciudad.agregar_edificio(edificio2)
ciudad.agregar_vehiculo(vehiculo1)
ciudad.agregar_vehiculo(vehiculo2)

# Probar métodos y propiedades
print(ciudadano1.mostrar_ciudadano)
ciudadano1.trabajar()
print(f"Después de trabajar, dinero de {ciudadano1.nombre}: {ciudadano1.dinero}")

print(ciudadano2.mostrar_ciudadano)
ciudadano2.renunciar_trabajo()
print(f"Después de renunciar, trabajo de {ciudadano2.nombre}: {ciudadano2.trabajo}")

print(f"Ciudad: {ciudad}")
for ciudadano in ciudad.ciudadanos:
    print(ciudadano.mostrar_ciudadano)
for edificio in ciudad.edificios:
    print(edificio)
for vehiculo in ciudad.vehiculos:
    print(vehiculo)