# try, except, else e finally
try:
    a=18
    b=0
    # print('b[0]')
    print('Linha 1'[1000])
    c = a/b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero')
except  NameError:
    print('Alguma variável não foi definida')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
    
except Exception:
    print ('ERRO DESCONHECIDO')

print('Continuar')