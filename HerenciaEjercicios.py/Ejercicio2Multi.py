class Administrativo:
    def gestionar_documentos(self):
        print("Gestionando documentos... revisando archivos y organizando registros.")

class Tecnico:
    def resolver_problemas(self):
        print("Resolviendo problemas técnicos... diagnosticando y aplicando soluciones.")

class Asistente(Administrativo, Tecnico):
    def trabajo_diario(self):
        print("Iniciando jornada laboral:")
        self.gestionar_documentos()
        self.resolver_problemas()
        print("Jornada completada con éxito!")

asistente = Asistente()
asistente.trabajo_diario()