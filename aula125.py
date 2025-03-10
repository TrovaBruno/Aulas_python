class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa ('Bruno', 19)

print(p1.get_ano_de_nascimento())
        