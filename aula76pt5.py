# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

dicionario_bruno = {
    'nome': 'Bruno',
    'sobrenome': 'Trova',
    'idade': 18
}

# nome = dicionario_bruno.pop('nome')
# print(nome)
# print(dicionario_bruno)

# ultima_chave = dicionario_bruno.popitem()
# print(ultima_chave)
# print(dicionario_bruno)

# dicionario_bruno.update ({
#     'cursando': 'Sistemas da Informação',
#     'sobrenome': 'Campaner Trova'
# })
# print(dicionario_bruno)

# tupla = (('nome', 'Bruno Campaner Trova'), ('idade', 19))
# dicionario_bruno.update(tupla)
# print(dicionario_bruno)

lista = [['nome', 'Bruninho Campaner'], ['idade', 30]]
dicionario_bruno.update(lista)
print(lista)