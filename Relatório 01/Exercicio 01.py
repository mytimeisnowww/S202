class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f"O aluno {self.nome} está presente."


class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        lista_presenca = [aluno.presenca() for aluno in self.alunos]
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n" + "\n".join(lista_presenca)


if __name__ == "__main__":
    prof = Professor("João")

    
    aluno1 = Aluno("Maria")
    aluno2 = Aluno("José")
    aluno3 = Aluno("Ana")

    aula = Aula(prof, "Orientação a Objetos")
    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    aula.adicionar_aluno(aluno3)

    print(aula.listar_presenca())