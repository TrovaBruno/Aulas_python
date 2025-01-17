string = 'Bruno Campaner Trova'
grupo_de_letra = 3

nova_string = '.'.join([
    string[indice:indice + grupo_de_letra]
    for indice in range(0, len(string), grupo_de_letra)
])

print(nova_string)