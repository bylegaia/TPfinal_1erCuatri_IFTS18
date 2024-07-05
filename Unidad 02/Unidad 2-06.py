"""  Implementa un sistema de reservas para un cine que permita a los usuarios reservar asientos para películas. Debe haber clases como Pelicula, SalaCine, Reserva, etc """

class Cine:
    def __init__(self, nombre, direccion, salas):
        self.nombre = nombre
        self.direccion = direccion
        self.salas_cine = []
        for sala in salas:
            self.salas_cine.append(SalaCine(**sala))

    def seleccionar_sala(self, numero):
        for sala in self.salas_cine:
            if sala.numero == numero:
                return sala

    def __str__(self) -> str:
        return f"{self.nombre} ubicado en {self.direccion}"

class SalaCine:
    def __init__(self, numero, cantidad_asientos):
        self.numero = numero
        self.cantidad_asientos = cantidad_asientos
        self.pelicula_programada = None
    
    @property
    def mostrar_asientos(self):
        return self.cantidad_asientos

    def programar_pelicula(self, pelicula_a_proyectar):
        self.pelicula_programada = Pelicula(**pelicula_a_proyectar)

    def desprogramar_pelicula(self):
        self.pelicula_programada = None

    @property
    def mostrar_pelicula_programada(self):
        return self.pelicula_programada
    
    @property
    def mostrar_estado_sala(self):
        confirmado_pelicula = f"va a proyectar {self.pelicula_programada}" if self.pelicula_programada != None else "hoy no tiene pelicula programada"
        return f"Sala {self.numero} {confirmado_pelicula}\n La sala cuenta con {self.cantidad_asientos} asientos"
    
    def __str__(self) -> str:
        return f"Sala {self.numero}"

class Pelicula:
    def __init__(self, nombre, duracion, genero, clasificacion: bool):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.clasificacion = "ATP" if clasificacion == True else "+18"

    @property
    def mostrar_pelicula(self):
        return f"Nombre: {self.nombre}\nDuracion: {self.duracion} minutos\nGenero: {self.genero}\nClasificacion: {self.clasificacion}"
    
    def __str__(self) -> str:
        return self.nombre
    
class ReservarAsientos:
    def __init__(self, sala):
        self.sala = sala
        self.cantidad_asientos_disponibles = sala.mostrar_asientos
        self.pelicula_programada = sala.mostrar_pelicula_programada

    def reservar_asientos(self, cantidad_a_reservar):
        if self.pelicula_programada != None:
            if cantidad_a_reservar <= self.cantidad_asientos_disponibles:
                self.cantidad_asientos_disponibles -= cantidad_a_reservar
                return f"{cantidad_a_reservar} asientos reservados con exito"
            else:
                return "Ya no hay asientos disponibles"
        return "No hay una pelicula programada a la que reservar asientos"
    
    @property
    def mostrar_asientos_disponibles(self):
        return self.cantidad_asientos_disponibles
    
    @property
    def mostrar_estado_reservas(self):
        return f"Se han reservado {self.sala.mostrar_asientos - self.cantidad_asientos_disponibles} asientos en la {self.sala} donde se va a proyectar {self.pelicula_programada}" if self.pelicula_programada != None else "Hoy no hay pelicula a la que reservar asientos"
    


""" Aca volvi a pedirle ejemplos a chatgpt y otra vez se lo tuve que corregir e.e """



# Ejemplos de uso

# Crear películas
pelicula1 = {"nombre": "Avengers: Endgame", "duracion": 180, "genero": "Acción", "clasificacion": True}
pelicula2 = {"nombre": "Toy Story 4", "duracion": 100, "genero": "Animación", "clasificacion": True}
pelicula3 = {"nombre": "The Godfather", "duracion": 175, "genero": "Drama", "clasificacion": True}

# Crear salas de cine
sala1 = {"numero": 1, "cantidad_asientos": 50}
sala2 = {"numero": 2, "cantidad_asientos": 80}

cine = Cine("Cinemark", "asd 123", [sala1, sala2])

# Programar películas en las salas
sala_cine1 = cine.seleccionar_sala(1)
sala_cine1.programar_pelicula(pelicula1)

sala_cine2 = cine.seleccionar_sala(2)
sala_cine2.programar_pelicula(pelicula2)

# Crear instancia de ReservarAsientos para cada sala
reserva_sala1 = ReservarAsientos(sala_cine1)
reserva_sala2 = ReservarAsientos(sala_cine2)

# Ejemplo de reserva de asientos
print(reserva_sala1.reservar_asientos(3))
print(reserva_sala1.reservar_asientos(5))
print(reserva_sala1.reservar_asientos(1))
print(reserva_sala2.reservar_asientos(5))

# Mostrar estado de las reservas y asientos disponibles
print(reserva_sala1.mostrar_estado_reservas)
print(reserva_sala2.mostrar_estado_reservas)

sala_cine2.programar_pelicula(pelicula3)
reserva_sala2 = ReservarAsientos(sala_cine2)

print(reserva_sala2.reservar_asientos(5))
print(reserva_sala2.mostrar_estado_reservas)