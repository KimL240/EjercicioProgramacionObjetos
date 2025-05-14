class Persona:
    def _init_(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

class Evento:
    def _init_(self, tipo_evento, fecha):
        self.tipo_evento = tipo_evento
        self.fecha = fecha

class Coordinador(Persona, Evento):
    def _init_(self, nombre, rol, tipo_evento, fecha):
        Persona._init_(self, nombre, rol)
        Evento._init_(self, tipo_evento, fecha)
    
    def mostrar_evento(self):
        print("--- Detalles del Evento ---")
        print(f"Coordinador: {self.nombre}")
        print(f"Rol: {self.rol}")
        print(f"Tipo de evento: {self.tipo_evento}")
        print(f"Fecha: {self.fecha}")

evento=Coordinador("Carlos Ruiz", "Coordinador Principal","Conferencia Anual", 2023-11-15)
evento.mostrar_evento()