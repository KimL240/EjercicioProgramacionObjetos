class Temperatura:
    def __init__(self, valor, escala='C'):
        self.valor = valor
        self.escala = escala.upper()
    
    def a_fahrenheit(self):
        if self.escala == 'C':
            resultado = (self.valor * 9/5) + 32
            print(f"{self.valor}°C equivalen a {resultado:.2f}°F")
        else:
            print(f"La temperatura ya está en Fahrenheit: {self.valor}°F")
    
    def a_celsius(self):
        if self.escala == 'F':
            resultado = (self.valor - 32) * 5/9
            print(f"{self.valor}°F equivalen a {resultado:.2f}°C")
        else:
            print(f"La temperatura ya está en Celsius: {self.valor}°C")
    
    def mostrar(self):
        print(f"Temperatura actual: {self.valor}°{self.escala}")

temp1 = Temperatura(25)  
temp1.mostrar()    
temp1.a_fahrenheit() 
