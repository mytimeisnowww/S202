from AutorCRUD import AutorCRUD
from LivroCRUD import LivroCRUD
from database import Database

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://35.170.71.35:7687", "neo4j", "ports-hunk-bulkheads")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
livro_db = LivroCRUD(db)
autor_db = AutorCRUD(db)

escolha = input("Faça sua escolha\n"
                "1 - Criar Autor\n"
                "2 - Ler Autor\n"
                "3 - Atualizar Autor\n"
                "4 - Deletar Autor\n"
                "5 - Criar Livro\n"
                "6 - Ler Livro\n"
                "7 - Atualizar Livro\n"
                "8 - Deletar Livro\n"
                "9 - Associar livro ao autor\n"
                "10 - Livros do Autor\n"
                "11 - Média de páginas dos Livros\n"
                "0 - Sair\n"
                )

while escolha != "0":

    if escolha == "1":
        nome = input("Nome do Autor: ")
        idade = input("Idade do Autor: ")
        genero = input("Gênero do Autor: ")
        autor_db.criar_autor(nome, idade, genero)

    if escolha == "2":
        print("Autores")
        print("--------------------")
        autor_db.obter_autor()
        print("--------------------\n")

    if escolha == "3":
        nome = input("Nome do Autor: ")
        idade = input("Nova idade: ")
        genero = input("Novo gênero: ")
        autor_db.atualizar_autor(nome, idade, genero)

    if escolha == "4":
        nome = input("Nome do Autor:")
        autor_db.deletar_autor(nome)

    if escolha == "5":
        nome = input("Nome do Livro: ")
        paginas = input("Número de páginas do Livro: ")
        genero = input("Gênero do Livro: ")
        livro_db.criar_livro(nome, paginas, genero)

    if escolha == "6":
        print("Livros")
        print("--------------------")
        livro_db.obter_livro()
        print("--------------------\n")

    if escolha == "7":
        nome = input("Nome do Livro: ")
        paginas = input("Novas páginas: ")
        genero = input("Novo gênero: ")
        livro_db.atualizar_livro(nome, paginas, genero)

    if escolha == "8":
        nome = input("Nome do Livro: ")
        livro_db.deletar_livro(nome)

    if escolha == "9":
        nome_autor = input("Nome do Autor: ")
        nome_livro = input("Nome do Livro: ")
        autor_db.inserir_livro_autor(nome_autor, nome_livro)

    if escolha == "10":
        nome = input("Nome do Autor: ")
        print("Livros de", nome + ":")
        print("--------------------")
        print(autor_db.obter_livros_escritos(nome))
        print("--------------------\n")

    if escolha == "11":
        print("--------------------")
        print("Média de páginas dos livros:")
        print(livro_db.obter_media_paginas_livros())
        print("--------------------\n")

    escolha = input("Faça sua escolha\n"
                    "1 - Criar Autor\n"
                    "2 - Ler Autor\n"
                    "3 - Atualizar Autor\n"
                    "4 - Deletar Autor\n"
                    "5 - Criar Livro\n"
                    "6 - Ler Livro\n"
                    "7 - Atualizar Livro\n"
                    "8 - Deletar Livro\n"
                    "9 - Associar livro ao autor\n"
                    "10 - Livros do Autor\n"
                    "11 - Média de páginas dos Livros\n"
                    "0 - Sair\n")
