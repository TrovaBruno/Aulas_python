# reduce - faz a redução de um iterável em um valor
from functools import reduce 

produtos = [ 
   {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto ['preco']

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos, 
    0
)

print('Total é', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)
# print(sum([p['preco']for p in produtos]))



# A função reduce faz parte do módulo functools no Python e é usada para aplicar uma função cumulativa a 
# uma sequência de elementos, reduzindo-a a um único valor. Essencialmente, ela aplica uma função passada 
# como argumento aos elementos da sequência de maneira acumulativa, isto é, o resultado da função é usado 
# como um dos argumentos da função para o próximo elemento na sequência.