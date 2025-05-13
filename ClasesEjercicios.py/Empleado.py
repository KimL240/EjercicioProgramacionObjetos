class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_salario_anual(self):
        salario_anual = self.salario * 12
        print(f'Empleado: {self.nombre}')
        print(f'Salario mensual: ${self.salario:,.2f}')
        print(f'Salario anual: ${salario_anual:,.2f}')
        
Empleado1=Empleado('Jose López', 2500.75)
Empleado1.calcular_salario_anual()
