from Corrida import Corrida
from MotoristaDAO import MotoristaDAO
from Passageiro import Passageiro


class MotoristaCLI:
    def __init__(self):
        self.motorista = MotoristaDAO()
        self.menu()

    def menu(self):
        print("Bem-vindo ao sistema de gerenciamento de motoristas!")
        while True:
            print("\nOptions:")
            print("1. Create")
            print("2. Read")
            print("3. Update")
            print("4. Delete")
            print("0. Exit")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Crie um passageiro:\n")
                nome = input("Digite o nome do passageiro\n")
                documento = input("Digite o documento do passageiro\n")
                p = Passageiro(nome, documento)
                print("Crie uma corrida:\n")
                op = "1"
                corridas = []
                while op != "0":
                    distancia = input("Distancia:\n")
                    valor = input("Valor:\n")
                    nota = input("Nota:\n")
                    c = Corrida(distancia, valor, p, nota)
                    corridas.append(c)
                    op = input("Para inserir outra corrida digite qualquer coisa, senão digite 0\n")
                n1 = input("Digite uma nota para o motorista\n")
                self.motorista.create_motorista(corridas, n1)

            elif opcao == "2":
                id = input("Digite o id do motorista:\n")
                self.motorista.read_motorista(id)
            elif opcao == "3":
                nota = input("Digite a nota:\n")
                novos_dados = {"nota": nota}
                id = input("Digite o ID do motorista:\n")
                self.motorista.update_motorista(id, novos_dados)

            elif opcao == "4":
                id = input("Digite o ID do motorista:\n")
                self.motorista.delete_motorista(id)
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
