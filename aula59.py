# Desempacotamento em chamadas
#de métodos e funções

string ='ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap = lista
# print(p,ap) ==================> saida Maria Eduarda

print(*string)
print(*lista)
print(*tupla)