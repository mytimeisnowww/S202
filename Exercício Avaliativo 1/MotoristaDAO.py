from bson import ObjectId


from database import Database


class MotoristaDAO:
    def __init__(self):
        self.db = Database(database="atlas-cluster", collection="motoristas")

    def create_motorista(self, corridas, nota):
        try:
            motorista_data = []
            for corrida in corridas:
                motorista_data.append({
                    "id": str(corrida.id),
                    "valor": corrida.valor,
                    "distancia": corrida.distancia,
                    "nota": corrida.nota,
                    "passageiro": {
                        "id": str(corrida.passageiro.id),
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                })

            motorista_data = {
                "corridas": motorista_data,
                "nota": nota
            }
            res = self.db.collection.insert_one(motorista_data)
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating person: {e}")
            return None

    def read_motorista(self, motorista_id):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(motorista_id)})
            if motorista:
                print("Motorista encontrado:")
                print(motorista)
            else:
                print("Motorista não encontrado.")
        except Exception as e:
            print(f"Erro ao ler motorista: {e}")

    def update_motorista(self, motorista_id, novos_dados):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": novos_dados})
            if res.modified_count > 0:
                print("Motorista atualizado com sucesso.")
            else:
                print("Nenhum motorista foi atualizado.")
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")

    def delete_motorista(self, motorista_id):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(motorista_id)})
            if res.deleted_count > 0:
                print("Motorista excluído com sucesso.")
            else:
                print("Nenhum motorista foi excluído.")
        except Exception as e:
            print(f"Erro ao excluir motorista: {e}")
