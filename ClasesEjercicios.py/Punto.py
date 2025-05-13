class punto:
    def __init__(sefl,x,y):
        sefl.x=x
        sefl.y=y
    def calcular_distancia(self):
        resultado= self.x*{self.y * 100}
        return f'Y: Es una distancia de {self.y} metros cuanto es centimetro "x" para llegar a y : {resultado} es la distancia que necesita'
      
punto1=punto(10, 50)
print(punto1.calcular_distancia())