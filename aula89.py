# dir, hasattr e getattr em python

string = 'Luiz'
metodo = 'upper'

if hasattr (string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())

else:
    print ('Não existe o método', metodo)
# hasattr usada para verificar se um objeto tem um determinado atributo. Basicamente, ela retorna True se o objeto tiver o atributo especificado e False se não tiver.
# getattr usada para acessar o valor de um atributo de um objeto. Se o atributo não existir, você pode especificar um valor padrão para ser retornado, em vez de levantar um erro.

