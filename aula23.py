# Operadores in e not in
#Strings são iteraveis
# O T A V I O
# 0 1 2 3 4 5
#-6-5-4-3-2-1


"""
nome = 'Otavio'
print ('vio' in nome) #'vio' está em nome? true 
print ('lad' in nome) #'lad' está em nome? false

print(10 * '-')

print('vio' not in nome) #'vio' não está em nome? false
print('lad' not in nome) #'lad' não está em nome? true
"""

nome = input("Digite seu nome: ")
encontrar  = input("Digite o que deseja encontrar: ")

if encontrar in nome: 
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')