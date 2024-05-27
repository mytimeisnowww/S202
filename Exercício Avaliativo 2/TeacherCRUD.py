from database import Database


class TeacherCRUD:
    def __init__(self):
        # cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
        self.db = Database("bolt://44.193.1.152:7687", "neo4j", "specialties-minority-motels")

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name,ano_nasc: $ano_nasc,cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = (
            "MATCH (t:Teacher) WHERE t.name CONTAINS $name "
            "RETURN t.name AS name, t.cpf AS cpf, t.ano_nasc AS ano_nasc"
        )
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [{"name": result["name"], "ano_nasc": result["ano_nasc"], "cpf": result["cpf"]} for result in results]

    def update(self, name, cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $cpf"
        parameters = {"name": name, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
