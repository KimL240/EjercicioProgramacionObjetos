class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Carrera: {self.carrera}")

estudiante = Estudiante("Carlos Méndez", 22, "Ingeniería Informática")
estudiante.mostrar_datos()