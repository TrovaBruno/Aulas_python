a = '1.1'
b = 'BBB'
c= 'Eu torço para o São Paulo Futebol Clube'
'''
teste = 'a = {} b = {} c = {}'
format = teste.format(a,b,c)
'''
# podemos usar a função format para chamar variáveis da forma acima
'''
teste = 'a = {0} b = {1} c = {2}'
format = teste.format(a,b,c)
'''

# seguindo as ordens das variáveis que estão dentro dos parenteses, a = 0, b=1 c=2, 
#conseguimos chamar elas colocando no parametro esses indices

teste = 'a = {nome1} b = {nome1} c = {nome3}'
format = teste.format(nome1=a,nome2=b,nome3=c)

print(format)

#Nós podemos nomear as variáveis da forma como mostrada acima, para chama-las atráves
#de seus nomes. PODEMOS TAMBÉM COLOCAR O :.2f para formatar as casas decimais quando necessário






