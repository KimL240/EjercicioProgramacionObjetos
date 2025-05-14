class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Proyecto:
    def _init_(self, nombre_proyecto, duracion):
        self.nombre_proyecto = nombre_proyecto
        self.duracion = duracion

class ProjectManager(Persona, Proyecto):
    def _init_(self, nombre, edad, nombre_proyecto, duracion):
        Persona._init_(self, nombre, edad)
        Proyecto._init_(self, nombre_proyecto, duracion)
    
    def mostrar_informacion(self):
        print(f"Project Manager: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Proyecto: {self.nombre_proyecto}")
        print(f"Duración: {self.duracion} meses")


persona1=ProjectManager("Laura Gómez", 35, "Sistema ERP", 6)
persona1.mostrar_informacion()