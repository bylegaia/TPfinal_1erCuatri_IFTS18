"""  Implementa un sistema de gestión de inventario para una tienda que incluya clases como Producto, Inventario, Proveedor, etc. El inventario debe ser capaz de realizar operaciones como agregar productos, actualizar existencias, etc """

class Producto:
    def __init__(self, nombre, precio, proveedor):
        self.nombre = nombre
        self._precio = precio
        self._stock = 1
        self.proveedor = Proveedor(**proveedor)
        self.tipo = self.proveedor.tipo

    @property
    def mostrar_precio(self):
        return self._precio
    
    @property
    def mostrar_stock(self):
        return self._stock
    
    def modificar_precio(self, nuevo_precio):
        self._precio = nuevo_precio if nuevo_precio >= 0 else self._precio
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nPrecio: ${self._precio}\nCantidad: {self._stock}\nTipo de producto: {self.tipo}"
    
class Proveedor:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nTipo de Productos: {self.tipo}"
    
class Inventario:
    def __init__(self):
        self.productos_disponibles = []
    
    @property
    def mostrar_stock(self):
        return self.productos_disponibles
    
    def agregar_producto(self, producto_nuevo):
        self.productos_disponibles.append(Producto(**producto_nuevo))

    def actualizar_existencias(self, producto_a_modificar, modificar_stock):
        for producto in self.productos_disponibles:
            if producto.nombre == producto_a_modificar:
                nuevo_stock = producto.mostrar_stock + modificar_stock
                producto.mostrar_stock = nuevo_stock if nuevo_stock >= 0 else producto.mostrar_stock
                break

    def eliminar_producto(self, producto_a_eliminar):
        for producto in self.productos_disponibles:
            if producto.nombre == producto_a_eliminar:
                self.productos_disponibles.remove(producto)

proveedor = {
    "nombre": "Corsair",
    "tipo": "Periferico PC"
}

producto1 = {
    "nombre": "Teclado k70",
    "precio": 26999,
    "proveedor": proveedor
}

producto2 = {
    "nombre": "Mouse Harpoon Pro",
    "precio": 14999,
    "proveedor": proveedor
}

stock = Inventario()

stock.agregar_producto(producto1)
stock.agregar_producto(producto2)

for producto in stock.mostrar_stock:
    print("-" * 30)
    print(producto)
print("-" * 30)

stock.actualizar_existencias("Teclado k70", +5)

for producto in stock.mostrar_stock:
    print("-" * 30)
    print(producto)
print("-" * 30)

stock.eliminar_producto("Teclado k70")

for producto in stock.mostrar_stock:
    print("-" * 30)
    print(producto)
print("-" * 30)