""" Crea una clase llamada Producto que tenga atributos como nombre, precio y cantidad_disponible. Implementa métodos para actualizar la cantidad disponible y para mostrar la información del producto """

class Producto:
    def __init__(self, nombre, precio: int, cantidad_disponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def mostrar_informacion(self) -> str:
        return f"Nombre: {self.nombre} \nPrecio: ${self.precio} \nStock Disponible: {self.cantidad_disponible}"
    
    # def actualizar_cantidad(self, cambio_cantidad: int) -> int:
    #     nueva_cantidad = cambio_cantidad + self.cantidad_disponible
    #     if nueva_cantidad < 0:
    #         return self.cantidad_disponible
    #     else:
    #         self.cantidad_disponible = nueva_cantidad
    #         return self.cantidad_disponible
        
    def actualizar_cantidad2(self, cambio_cantidad: int) -> int:
        nueva_cantidad = cambio_cantidad + self.cantidad_disponible # juntamos la cantidad a cambiar y la cantidad disponible
        if nueva_cantidad >= 0:                                     # Si la combinacion de las 2 variables es mayor o igual a 0
            self.cantidad_disponible = nueva_cantidad               # Procede a modificar el atributo
            return self.cantidad_disponible
        # en caso contrario no hace nada y deja el atributo sin modificar

producto1 = Producto("Teclado", 2500, 10)

print(producto1.mostrar_informacion())
producto1.actualizar_cantidad2(-5)
print(producto1.mostrar_informacion())
producto1.actualizar_cantidad2(20)
print(producto1.mostrar_informacion())
producto1.actualizar_cantidad2(-50)
print(producto1.mostrar_informacion())