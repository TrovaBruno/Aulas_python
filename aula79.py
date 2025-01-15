letras = set()

while True:
    letra=input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS, VOCÊ ENCONTROU A LETRA CORRETA')
        break

    print(letras)
