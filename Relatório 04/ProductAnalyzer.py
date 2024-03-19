from database import Database


class ProductAnalyzer:
    def __init__(self, db: Database):
        self.db = db

    def totalDeVendas(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra","total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}},"total_produtos": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id": 1}}
        ])
        return result

    def produtoMaisVendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return result

    def clienteQueMaisGastou(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id","total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        return result

    def produtosQueTiveramUmaQuantidadeVendidaAcimaDe1Unidades(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_total_vendida": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade_total_vendida": {"$gt": 1}}}
        ])
        return result
