from neo4j import GraphDatabase


class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data


class Neo4jClient(Database):
    def __init__(self, uri, user, password):
        super().__init__(uri, user, password)

    def is_engenheiro(self, pessoa_nome):
        query = (
            "MATCH (p:Pessoa {nome: $nome})-[:PROFISSAO]->(profissao:Profissao {nome: 'Engenheiro'}) "
            "RETURN p.nome"
        )
        result = self.execute_query(query, parameters={"nome": pessoa_nome})
        return len(result) > 0

    def pai_de_quem(self, pessoa_nome):
        query = (
            "MATCH (p:Pessoa {nome: $nome})-[:PAI_DE]->(filho) "
            "RETURN filho.nome"
        )
        result = self.execute_query(query, parameters={"nome": pessoa_nome})
        return [record["filho.nome"] for record in result]

    def tem_pet(self):
        query = (
            "MATCH (p:Pessoa)-[:TEM_COMO_ANIMAL_DE_ESTIMACAO]->(pet) "
            "RETURN p.nome, pet.nome"
        )
        result = self.execute_query(query)
        return [(record["p.nome"], record["pet.nome"]) for record in result]
