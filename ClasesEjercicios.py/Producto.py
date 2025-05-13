class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        precio_con_descuento = self.precio - descuento
        print(f"Precio original: ${self.precio:.2f}")
        print(f"Descuento ({porcentaje}%): ${descuento:.2f}")
        print(f"Precio con descuento: ${precio_con_descuento:.2f}")
producto1 = Producto("Zapatillas deportivas", 120.00)
producto1.aplicar_descuento(15)
