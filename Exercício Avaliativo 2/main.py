from TeacherCRUD import TeacherCRUD


def main():
    teacher_crud = TeacherCRUD()
    while True:
        print("\n1. Criar novo professor")
        print("2. Pesquisar professor por nome")
        print("3. Atualizar CPF de um professor")
        print("4. Deletar professor por nome")
        print("5. Sair")

        choice = input("\nEscolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome do professor: ")
            ano_nasc = input("Digite o ano de nascimento: ")
            cpf = input("Digite o CPF: ")
            teacher_crud.create(name, ano_nasc, cpf)
            print("Professor criado com sucesso!")

        elif choice == '2':
            name = input("Digite o nome do professor: ")
            result = teacher_crud.read(name)
            if result:
                print("Professor encontrado:")
                print(f"Nome: {result[0]['name']}")
                print(f"Ano de nascimento: {result[0]['ano_nasc']}")
                print(f"CPF: {result[0]['cpf']}")
            else:
                print("Professor não encontrado.")

        elif choice == '3':
            name = input("Digite o nome do professor: ")
            new_cpf = input("Digite o novo CPF: ")
            teacher_crud.update(name, new_cpf)
            print("CPF atualizado com sucesso!")

        elif choice == '4':
            name = input("Digite o nome do professor: ")
            teacher_crud.delete(name)
            print("Professor deletado com sucesso!")

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
