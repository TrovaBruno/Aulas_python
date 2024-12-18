for i in range (10):
    if i ==2:
        print('i é 2, pulando')
        continue

    if i == 8:
        print ('i é 8, seu else não executará')
        break

    for j in range (5,9): #O loop for j in range(5, 9) faz com que j assuma os valores de 5 a 8 (inclusive).
# Impressão de i e j:
# Para cada valor de i no loop principal, o loop aninhado imprime a combinação atual de i e j.
# Exemplo de Saída:
# Se i for 1, o loop aninhado imprimirá:
# 1 5
# 1 6
# 1 7
# 1 8
        print(i,j)

else:
    print('For completo com sucesso!')