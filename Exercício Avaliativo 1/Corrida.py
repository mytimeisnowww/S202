from bson import ObjectId


class Corrida:
    def __init__(self, distancia, valor, passageiro, nota):
        self.id = ObjectId()
        self.distancia = float(distancia)
        self.valor = float(valor)
        self.passageiro = passageiro
        self.nota = int(nota)
