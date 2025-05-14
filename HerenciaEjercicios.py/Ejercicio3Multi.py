class Sensor:
    def _init_(self, tipo_sensor):
        self.tipo_sensor = tipo_sensor

class Conexion:
    def _init_(self, protocolo):
        self.protocolo = protocolo

class Alerta(Sensor, Conexion):
    def _init_(self, tipo_sensor, protocolo, nivel_alerta):
        Sensor._init_(self, tipo_sensor)
        Conexion._init_(self, protocolo)
        self.nivel_alerta = nivel_alerta
    
    def mostrar_datos(self):
        print(f"Sensor: {self.tipo_sensor}")
        print(f"Protocolo: {self.protocolo}")
        print(f"Nivel de alerta: {self.nivel_alerta}")
        print("Transmitiendo datos meteorológicos...")

alerta = Alerta("Termohigrómetro", "MQTT", "Amarillo")
alerta.mostrar_datos()