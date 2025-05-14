class Producto:
    def _init_(self, nombre, lote):
        self.nombre = nombre
        self.lote = lote

class Evaluacion:
    def _init_(self, resultado, observaciones):
        self.resultado = resultado  # Aprobado/Rechazado
        self.observaciones = observaciones

class InformeCalidad(Producto, Evaluacion):
    def _init_(self, nombre, lote, resultado, observaciones):
        Producto._init_(self, nombre, lote)
        Evaluacion._init_(self, resultado, observaciones)
    
    def resumen_inspeccion(self):
        print("=== Informe de Calidad ===")
        print(f"Producto: {self.nombre}")
        print(f"Lote: {self.lote}")
        print(f"Resultado: {self.resultado}")
        print("Observaciones:")
        print(self.observaciones)
        print("="*25)

informe = InformeCalidad("Smartphone", 2023-45,"Aprobado", "El producto cumple con todos los estándares de calidad.")
informe.resumen_inspeccion()