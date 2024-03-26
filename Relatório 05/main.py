from database import Database
from livroModel import LivroModel

db = Database(database="Relatorio_05", collection="Livros")
livroModel = LivroModel(database=db)

# livroModel.criar_livro(3,"The Lord of the Rings: The Fellowship of the Ring","J.R.R. Tolkien.",1954, 69.99)

# livroModel.ler_livro_por_id(2)

# livroModel.atualizar_livro(2,"Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999, 33.33)

# livroModel.deletar_livro(1)

while True:
    print("\nMenu:")
    print("1. Criar livro")
    print("2. Ler livro por ID")
    print("3. Atualizar livro")
    print("4. Deletar livro")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        _id = int(input("Digite o id do livro: "))
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano do livro: "))
        preco = float(input("Digite o preço do livro: "))
        livroModel.criar_livro(_id, titulo, autor, ano, preco)

    elif opcao == "2":

        id_livro = input("Digite o ID do livro: ")

        try:

            id_livro = int(id_livro)

            livroModel.ler_livro_por_id(id_livro)

        except ValueError:

            print("O ID do livro deve ser um número inteiro.")

    elif opcao == "3":
        _id = int(input("Digite o ID do livro a ser atualizado: "))
        titulo = input("Digite o novo título do livro: ")
        autor = input("Digite o novo autor do livro: ")
        ano = int(input("Digite o novo ano do livro: "))
        preco = float(input("Digite o novo preço do livro: "))
        livroModel.atualizar_livro(_id, titulo, autor, ano, preco)

    elif opcao == "4":
        _id = int(input("Digite o ID do livro a ser deletado: "))
        livroModel.deletar_livro(_id)

    elif opcao == "5":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
