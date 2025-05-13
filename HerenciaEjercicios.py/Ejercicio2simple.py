# Gestión de Vehículos en una Empresa de Transporte

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print("El vehículo ha sido encendido")
    
    def mostrar_estado(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"Vehículo {estado}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje
    
    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cilindraje: {self.cilindraje} cc")
        self.mostrar_estado()

moto = Motocicleta("Yamaha", "MT-07", 689)
moto.encender()
moto.mostrar_datos()
