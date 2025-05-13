class Reloj:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.segundo = segundo % 60
        self.minuto = (minuto + segundo // 60) % 60
        self.hora = (hora + (minuto + segundo // 60) // 60) % 24
    
    def mostrar_hora(self):
        hora_formateada = f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'
        print(f'Hora actual: {hora_formateada}')
    
    def ajustar_hora(self, hora, minuto, segundo):
        self.__init__(hora, minuto, segundo)
        print('Hora ajustada correctamente.')

reloj1 = Reloj(8, 30, 0)
reloj1.mostrar_hora() 

