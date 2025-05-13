class Agenda:
    def __init__(self):
        self.contactos = {}
   
    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado correctamente.")
    
    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Nombre: {nombre}, Teléfono: {self.contactos[nombre]}")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")
    
    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("\n--- Lista de contactos ---")
            for nombre, telefono in sorted(self.contactos.items()):
                print(f"• {nombre}: {telefono}")
            print("-------------------------\n")

mi_agenda = Agenda()
mi_agenda.agregar_contacto("Isa Pérez", "555-1234567")
mi_agenda.agregar_contacto("Ruben García", "555-7654321")
mi_agenda.buscar_contacto("Juan Pérez")  
mi_agenda.buscar_contacto("Ana López")   

mi_agenda.mostrar_contactos()
