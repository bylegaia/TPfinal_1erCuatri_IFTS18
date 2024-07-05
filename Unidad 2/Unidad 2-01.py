""" Crea una clase llamada Producto que tenga atributos como nombre, precio y cantidad_disponible. Implementa métodos para actualizar la cantidad disponible y para mostrar la información del producto """

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self._precio = f"${precio}"
        self._cantidad_disponible = cantidad_disponible

    @property
    def mostrar_precio(self):
        return self._precio
    
    @property
    def mostrar_stock(self):
        return self._cantidad_disponible
    
    def modificar_precio(self, nuevo_precio):
        self._precio = f"${nuevo_precio}" if nuevo_precio >= 0 else self._precio
    
    def modificar_stock(self, modificar_stock):
        nuevo_stock = self._cantidad_disponible + modificar_stock
        self._cantidad_disponible = nuevo_stock if nuevo_stock >= 0 else self._cantidad_disponible

    def __str__(self):
        return f"Nombre: {self.nombre}\nPrecio: {self._precio}\nCantidad: {self._cantidad_disponible}"
    
asd = Producto("asd", 20, 5)

print(asd)
print("-" * 30)

print("Modifico el precio")
asd.modificar_precio(50)

print(asd.mostrar_precio)

print("Modifico el stock")
asd.modificar_stock(-4)

print(asd.mostrar_stock)

print("-" * 30)
print(asd)