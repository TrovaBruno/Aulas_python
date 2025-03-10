class Pessoa: 
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

print(vars(p1))
print(p1.nome)
print(p1.idade)