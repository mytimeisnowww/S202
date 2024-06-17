class LivroCRUD:
    def __init__(self, database):
        self.db = database

    def criar_livro(self, nome, paginas, genero):
        paginas = int(paginas)
        query = "CREATE (:Livro {nome: $nome, paginas: $paginas, genero: $genero})"
        parameters = {"nome": nome, "paginas": paginas, "genero": genero}
        self.db.execute_query(query, parameters)

    def obter_livro(self):
        query = "MATCH (l:Livro) RETURN l.nome AS nome"
        results = self.db.execute_query(query)
        return print([result["nome"] for result in results])

    def atualizar_livro(self, nome, paginas, genero):
        paginas = int(paginas)
        query = "MATCH (l:Livro {nome: $nome}) SET l.paginas = $paginas, l.genero = $genero"
        parameters = {"nome": nome, "paginas": paginas, "genero": genero}
        self.db.execute_query(query, parameters)

    def deletar_livro(self, nome):
        query = "MATCH (l:Livro {nome: $nome}) DETACH DELETE l"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def obter_media_paginas_livros(self):
        query = "MATCH (l:Livro) RETURN AVG(l.paginas) AS paginas"
        results = self.db.execute_query(query)
        return print([result["paginas"] for result in results])
