class AutorCRUD:
    def __init__(self, database):
        self.db = database

    def criar_autor(self, nome, idade, genero):
        query = "CREATE (:Autor {nome: $nome, idade: $idade, genero: $genero})"
        parameters = {"nome": nome, "idade": idade, "genero": genero}
        self.db.execute_query(query, parameters)

    def obter_autor(self):
        query = "MATCH (au:Autor) RETURN au.nome AS nome"
        results = self.db.execute_query(query)
        return print([result["nome"] for result in results])

    def atualizar_autor(self, nome, idade, genero):
        query = "MATCH (a:Autor {nome: $nome}) SET a.idade = $idade, a.genero = $genero"
        parameters = {"nome": nome, "idade": idade, "genero": genero}
        self.db.execute_query(query, parameters)

    def deletar_autor(self, nome):
        query = "MATCH (a:Autor {nome: $nome}) DETACH DELETE a"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def inserir_livro_autor(self, nome_autor, nome_livro):
        query = "MATCH (a:Autor {nome: $nome_autor}) MATCH (l:Livro {nome: $nome_livro}) CREATE (a)-[:ESCREVEU]->(l)"
        parameters = {"nome_autor": nome_autor, "nome_livro": nome_livro}
        self.db.execute_query(query, parameters)

    def obter_livros_escritos(self, nome):
        query = "MATCH (a:Autor{nome: $nome})-[:ESCREVEU]->(l:Livro) RETURN DISTINCT l.nome AS lnome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["lnome"] for result in results]
