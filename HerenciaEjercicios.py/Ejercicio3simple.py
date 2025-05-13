class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio base: ${self.precio:.2f}")


class ProductoImportado(Producto):
    def __init__(self, nombre, precio, impuesto):
        super().__init__(nombre, precio)
        self.impuesto = impuesto  # porcentaje
    
    def calcular_precio_final(self):
        return self.precio * (1 + self.impuesto / 100)
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Impuesto de importación: {self.impuesto}%")
        print(f"Precio final: ${self.calcular_precio_final():.2f}")

producto = ProductoImportado("Smartphone", 800, 15)
producto.mostrar_informacion()