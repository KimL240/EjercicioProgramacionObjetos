class calculadora:
    
    def __init__(self,sumar,restar,multiplicar,dividir):
        self.sumar=sumar
        self.restar=restar
        self.multiplicar=multiplicar
        self.dividir=dividir   
    def sumar(a,b):
        
        print(a+b)
        
    def restar(a,b):
        
        print(a-b)
        
    def multiplicar(a,b):
        
        print(a*b)
    
    def dividir(a,b):
        
        print(a/b)
        
print(calculadora.sumar(10,5))
print(calculadora.restar(75,8))
print(calculadora.multiplicar(45,6))
print(calculadora.dividir(58,10))    