# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(step=10, start=10)
r1 = range(10, 50, 10)

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('---------------')
print('range')
for i in r1:
    print(i)