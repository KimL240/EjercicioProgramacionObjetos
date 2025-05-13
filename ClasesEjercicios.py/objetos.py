class Laptop:
    
    def __init__(self,marca,pantalla,procesador,disco,memoria,color):
       self.marca=marca
       self.pantalla=pantalla
       self.procesador=procesador
       self.disco=disco
       self.memoria=memoria
       self.color=color
       
    def presentar(self):
        print(f'la marca es {self.marca} y es una gran marca')  
        
    def descuento(self):
        print(f'esta marca tiene un descuento del 15% por ser procesador{self.procesador}') 
        
laptop1=Laptop('hp','14','i5','250gb','8gb','rojo')
lapton2=Laptop('toshiba','15','i3','500gb','16','azul')
    
print(laptop1.marca, laptop1.procesador)

laptop1.presentar()
laptop1.descuento() 
    