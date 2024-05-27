from database import Database


class Queries:
    def __init__(self, uri, user, password):
        self.db = Database(uri, user, password)

    # Métodos da primeira questão

    def obter_informacoes_professor_renzo(self):
        query = """
        MATCH (p:Professor {nome: "Renzo"})
        RETURN p.ano_nasc AS ano_nasc, p.cpf AS cpf
        """
        return self.db.execute_query(query)

    def obter_professores_com_nome_inicial_m(self):
        query = """
        MATCH (p:Professor)
        WHERE p.nome STARTS WITH "M"
        RETURN p.nome AS nome, p.cpf AS cpf
        """
        return self.db.execute_query(query)

    def obter_nomes_todas_cidades(self):
        query = """
        MATCH (c:Cidade)
        RETURN c.nome AS nome_cidade
        """
        return self.db.execute_query(query)

    def obter_escolas_com_numero_especifico(self):
        query = """
        MATCH (e:Escola)
        WHERE e.número >= 150 AND e.número <= 550
        RETURN e.nome AS nome_escola, e.endereço AS endereço, e.número AS número
        """
        return self.db.execute_query(query)

    # Métodos da segunda questão

    def obter_ano_nascimento_professor_mais_jovem_e_mais_velho(self):
        query = """
        MATCH (p:Professor)
        RETURN min(p.ano_nasc) AS mais_jovem, max(p.ano_nasc) AS mais_velho
        """
        return self.db.execute_query(query)

    def obter_media_populacao_cidades(self):
        query = """
        MATCH (c:Cidade)
        RETURN avg(c.população) AS média_população
        """
        return self.db.execute_query(query)

    def obter_cidade_com_nome_modificado(self):
        query = """
        MATCH (c:Cidade {cep: "37540-000"})
        RETURN replace(c.nome, 'a', 'A') AS nome_modificado
        """
        return self.db.execute_query(query)

    def obter_terceira_letra_nomes_professores(self):
        query = """
        MATCH (p:Professor)
        RETURN substring(p.nome, 3, 1) AS terceira_letra
        """
        return self.db.execute_query(query)


if __name__ == "__main__":
    # URI do banco de dados Neo4j
    uri = "bolt://44.193.1.152:7687"
    user = "neo4j"
    passoword = "specialties-minority-motels"

    queries = Queries(uri, user, passoword)

    try:
        print("Questão 01:")
        informacoes_professor_renzo = queries.obter_informacoes_professor_renzo()
        print("Informações do Professor Renzo:")
        for registro in informacoes_professor_renzo:
            print(f"Ano de Nascimento: {registro['ano_nasc']}, CPF: {registro['cpf']}")
        print()

        professores_inicial_m = queries.obter_professores_com_nome_inicial_m()
        print("Professores cujo nome começa com 'M':")
        for registro in professores_inicial_m:
            print(f"Nome: {registro['nome']}, CPF: {registro['cpf']}")
        print()

        nomes_cidades = queries.obter_nomes_todas_cidades()
        print("Nomes de todas as cidades:")
        for registro in nomes_cidades:
            print(registro['nome_cidade'])
        print()

        escolas_numero_especifico = queries.obter_escolas_com_numero_especifico()
        print("Escolas com número entre 150 e 550:")
        for registro in escolas_numero_especifico:
            print(
                f"Nome da Escola: {registro['nome_escola']}, Endereço: {registro['endereço']}, Número: {registro['número']}")
        print()

        print("Questão 02:")
        ano_nascimento_mais_jovem_e_mais_velho = queries.obter_ano_nascimento_professor_mais_jovem_e_mais_velho()
        print("Ano de nascimento do professor mais jovem:", ano_nascimento_mais_jovem_e_mais_velho[0]['mais_jovem'])
        print("Ano de nascimento do professor mais velho:", ano_nascimento_mais_jovem_e_mais_velho[0]['mais_velho'])

        media_populacao = queries.obter_media_populacao_cidades()
        print("Média aritmética da população de todas as cidades:", media_populacao[0]['média_população'])

        cidade_nome_modificado = queries.obter_cidade_com_nome_modificado()
        print("Nome da cidade com 'a' substituído por 'A':", cidade_nome_modificado[0]['nome_modificado'])

        terceiras_letras = queries.obter_terceira_letra_nomes_professores()
        print("Terceira letra do nome de todos os professores:",
              [registro['terceira_letra'] for registro in terceiras_letras])

    finally:
        # Fechar a conexão com o banco de dados
        queries.db.close()
