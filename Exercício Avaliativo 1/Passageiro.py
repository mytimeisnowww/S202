from bson import ObjectId


class Passageiro:
    def __init__(self, nome, documento):
        self.id = ObjectId()
        self.nome = nome
        self.documento = documento
