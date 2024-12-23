"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e lostar valores da sua lista
Nãõ permita que o programa quebre com erros de indices inexistentes na lista
"""
import os
lista = []

while True:
    print('Selecione uma opção ')
    opcao = input('[i]nserir [a]pagar [l]istar ')

    if opcao == 'i':
        os.system('cls')
        valor =input('Valor: ')
        lista.append(valor)
        # print('i')

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except TypeError:
            print('Por favor digite numeros int.')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')


    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print (i, valor)
        # print('l')
    else: 
        print('Por favor, escolha i, a ou l.')