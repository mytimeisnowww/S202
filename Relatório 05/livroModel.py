from pymongo import MongoClient
from bson.objectid import ObjectId


class LivroModel:
    def __init__(self, database):
        self.db = database

    def criar_livro(self, _id: int, titulo: str, autor: str, ano: int, preco: float):
        try:
            self.db.collection.insert_one(
                {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com ID: {_id}")
            return _id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def ler_livro_por_id(self, id):
        try:
            # Se o ID for uma string, verificar se possui 24 caracteres
            if isinstance(id, str) and len(id) == 24:
                res = self.db.collection.find_one({"_id": ObjectId(id)})
            # Se o ID for um número, tentar converter para string e buscar
            elif isinstance(id, int):
                res = self.db.collection.find_one({"_id": id})
            else:
                raise ValueError("ID must be a 24-character hexadecimal string or an integer")

            if res:
                print(f"Livro encontrado: {res}")
                return res
            else:
                print("Livro não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao ler o livro: {e}")
            return None

    def atualizar_livro(self, _id: int, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.update_one({"_id": _id}, {
                "$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
            })

            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def deletar_livro(self, id: int):
        try:
            res = self.db.collection.delete_one({"_id": id})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None
