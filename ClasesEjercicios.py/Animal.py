class Animal:
    def hablar(self):
        print('Este animal hace un sonido')

class Perro(Animal):
    def hablar(self):
        print('¡Guau guau!')

class Gato(Animal):
    def hablar(self):
        print('¡Miau miau!')
        
Animal = Animal()
Perro = Perro()
Gato = Gato()

print('Sonidos de los animales:')
Animal.hablar()  
Perro.hablar()  
Gato.hablar()   