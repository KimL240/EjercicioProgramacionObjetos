 #Sistema de Recursos Humanos

class Empelados:
    def __init__(self,nombre, salario):
        self.nombre=nombre
        self.salario=salario
    def mostrar_informacion(self):
        print(f'Nombre{self.nombre}')
        print(f'Salario{self.salario}')


class Gerente(Empelados):
    def __init__(self, nombre, salario,departamento):
        Empelados.__init__(self,nombre, salario)
        self.departamento=departamento
    def mostrar_informacion(self):
         print(f'Nombre gerente {self.nombre} Departamento {self.departamento}')
    
Empelados1=Gerente('Jose martinez',2500,10)
Empelados1.mostrar_informacion()