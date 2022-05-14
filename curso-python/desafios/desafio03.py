"""
0 10
1 9
2 8
3 7
4 6
5 6
6 4
7 3
8 2
"""
#  WHILE
contador = 0
acumulador = 10

while contador < 9:
    print(contador, acumulador)
    contador += 1
    acumulador -= 1
print()

#  FOR
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
