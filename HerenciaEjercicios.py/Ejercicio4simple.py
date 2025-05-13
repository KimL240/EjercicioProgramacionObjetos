class Curso:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion  # en horas
    
    def mostrar_informacion(self):
        print(f"Curso: {self.titulo}")
        print(f"Duración: {self.duracion} horas")


class CursoVirtual(Curso):
    def __init__(self, titulo, duracion, plataforma):
        super().__init__(titulo, duracion)
        self.plataforma = plataforma
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Plataforma: {self.plataforma}")

curso = CursoVirtual("Python Avanzado", 40, "Udemy")
curso.mostrar_informacion()