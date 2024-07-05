"""  Crea una clase Producto con un método calcular_precio_descuento(). Luego, crea clases derivadas como ProductoDescuento, ProductoNormal, etc., quez implementen este método de manera diferente. """

class Producto:
    def __init__(self, nombre, descripcion, precio):
        self. nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def calcular_precio_descuento(self):
        pass

    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio Regular: ${self.precio}"
    
class ProductoDescuento(Producto):
    def __init__(self, nombre, descripcion, precio, descuento):
        super().__init__(nombre, descripcion, precio)
        self.descuento = descuento

    def calcular_precio_descuento(self, descuento):
        return self.precio - (self.precio * (descuento/100))
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}\n Descuento: {self.descuento}%\n Precio con Descuento: ${self.calcular_precio_descuento(self.descuento)}"
    
objeto1 = Producto("Mouse Corsair", "Mouse Pro de la marca Corsair", 15999)
objeto2 = ProductoDescuento("Joystick Xbox Series", "Joystick Original de la Cuarta Generacion de consolas de Microsoft, Xbox Series X|S", 39999, 25)

inventario = [objeto1, objeto2]

for objeto in inventario:
    print("-" * 30)
    print(f"{objeto.mostrar_info()}")
print("-" * 30)
