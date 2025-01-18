# Generator expression, Irerables e Iterators em Pytho
import sys

iterable = ['Eu', 'Tenho', '___iter___']
iterator = iter(iterable)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range(50)]
generator = (n for n in range(10))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
