def generator(n=0, maximum=10):
    # yield 1 #pausar
    # print('Continuando...')
    # yield 2 #pausar
    # print('Mais uma vez...')
    # yield 3 #pausar
    # print('Vou terminar')
    # return 'Acabou'
    while True:
        yield n
        n += 1

        if n > maximum:
            return
        
gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
for n in gen:
    print(n)