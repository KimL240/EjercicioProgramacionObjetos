 #Sistema de Recursos Humanos

class Empelados:
    def __init__(self,nombre, salario):
        self.nombre=nombre
        self.salario=salario
    def mostrar_informacion(self):
        print(f'Nombre:{self.nombre}')
        print(f'Salario : ${self.salario:.2f}')


class Gerente(Empelados):
    def __init__(self, nombre, salario,departamento):
        Empelados.__init__(self,nombre, salario)
        self.departamento=departamento
    def mostrar_informacion(self):
         print(f'Departamento {self.departamento}')
    
gerente=Gerente('Jose Martinez',2500,'ventas')
gerente.mostrar_informacion()