# try, except, else e finally
# o try tentará ser executado, já o finally sempre será executado
# o else acontece se o código não der erro
# pode ter quantos except que vc quiser

try:   
    print(1)
    8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('Não deu erro')

finally:
    print(2)