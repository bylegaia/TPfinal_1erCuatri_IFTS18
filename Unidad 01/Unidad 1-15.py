""" Crea una clase CarritoCompra que tenga una lista de productos. Usa agregación para representar la relación entre un carrito de compra y los productos que contiene. """

class CarritoCompra:
    def __init__(self, usuario, metodo_pago):
        self.usuario = usuario
        self.metodo_pago = metodo_pago if metodo_pago == "Tarjeta" or metodo_pago == "Efectivo" else None
        self._carrito = []

    @property
    def mostrar_carrito(self) -> list:
        return self._carrito
    
    def agregar_producto(self, producto_agregado):
        self._carrito.append(Producto(**producto_agregado))

    def quitar_producto(self, producto_eliminado):
        for producto in self._carrito:
            if producto_eliminado.get("nombre") == producto.nombre:
                self._carrito.remove(producto)

    def __str__(self) -> str:
        return f"Carrito a nombre de {self.usuario}"

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio
        self._stock = stock
        
    @property
    def mostrar_precio(self):
        return self._precio
    
    @property
    def mostrar_stock(self):
        return self._stock
    
    def modificar_precio(self, nuevo_precio):
        self._precio = nuevo_precio if nuevo_precio >= 0 else self._precio
    
    def modificar_stock(self, modificar_stock):
        nuevo_stock = self._stock + modificar_stock
        self._stock = nuevo_stock if nuevo_stock >= 0 else self._stock

    def __str__(self):
        return f"Nombre: {self.nombre}\nPrecio: ${self._precio}\nCantidad: {self._stock}"

producto1 = {
    "nombre": "Elden Ring",
    "precio": 51098,
    "stock": 10
}

producto2 = {
    "nombre": "Baldur's Gate",
    "precio": 53228,
    "stock": 15
}

producto3 = {
    "nombre": "Gunfire Reborn",
    "precio": 11957,
    "stock": 8
}

compra1 = CarritoCompra("Alejo Elalle", "Tarjeta")

compra1.agregar_producto(producto1)
compra1.agregar_producto(producto2)
compra1.agregar_producto(producto3)

print(compra1)
for producto in compra1.mostrar_carrito:
    print("-" * 30)
    print(producto)
print("-" * 30)

compra1.quitar_producto(producto2)

for producto in compra1.mostrar_carrito:
    print("-" * 30)
    print(producto)
print("-" * 30)