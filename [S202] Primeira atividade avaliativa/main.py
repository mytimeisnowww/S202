import threading
import time
import random
from pymongo import MongoClient


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

    def insert_data(self, sensor_name, sensor_value, unit, alarmed):
        try:
            data = {
                "nomeSensor": sensor_name,
                "valorSensor": sensor_value,
                "unidadeMedida": unit,
                "sensorAlarmado": alarmed
            }
            # Inserindo um novo documento na coleção
            self.collection.insert_one(data)
        except Exception as e:
            print(e)

    def update_alarm(self, sensor_name, alarmed):
        try:
            # Atualizando o campo "sensorAlarmado" no documento do sensor
            self.collection.update_one({"nomeSensor": sensor_name}, {"$set": {"sensorAlarmado": alarmed}})
        except Exception as e:
            print(e)


class Sensor(threading.Thread):
    def __init__(self, sensor_id, interval, db):
        super(Sensor, self).__init__()
        self.sensor_id = sensor_id
        self.sensor_name = f"Temp{sensor_id}"
        self.interval = interval
        self.db = db
        self.running = True
        self.alarmed = False

    def run(self):
        while self.running:
            if not self.alarmed:
                temperature = self.generate_temperature()
                if temperature > 38:
                    self.alarmed = True
                    self.db.update_alarm(self.sensor_name, self.alarmed)
                    print(f"Atenção! Temperatura muito alta! Verificar Sensor {self.sensor_name}!")
                self.db.insert_data(self.sensor_name, temperature, "°C", self.alarmed)
            time.sleep(self.interval)

    def generate_temperature(self):
        # Simulação de temperatura aleatória entre 30°C e 40°C
        return round(random.uniform(30, 40), 2)

    def stop(self):
        self.running = False


# Criando a instância do banco de dados
db = Database('bancoiot', 'sensores')
db.resetDatabase()  # Resetando o banco de dados

# Criando três sensores com intervalo de 2 segundos
sensor1 = Sensor(1, 2, db)
sensor2 = Sensor(2, 2, db)
sensor3 = Sensor(3, 2, db)

# Iniciando os sensores
sensor1.start()
sensor2.start()
sensor3.start()

try:
    # Executando indefinidamente
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Parando os sensores ao pressionar Ctrl+C
    sensor1.stop()
    sensor2.stop()
    sensor3.stop()
    sensor1.join()
    sensor2.join()
    sensor3.join()
    print("Sensores desligados.")
