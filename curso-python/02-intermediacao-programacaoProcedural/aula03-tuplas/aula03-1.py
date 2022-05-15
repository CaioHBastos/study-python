"""
Tuplas em Python
"""
tupla_1 = (1, 2, 3, 'a', 'Caio Bastos')
print(tupla_1)
print(tupla_1[4])

for valor in tupla_1:
    print(valor)

print(tupla_1[2:])


tupla_2 = 1, 2, 'a', 'b'
print(tupla_2)


tupla_3 = 1,
print(tupla_3)

tupla_4 = 1, 'S', 3, 4
tupla_5 = 5, 6, 7, 8
tupla_somada = tupla_4 + tupla_5
print(tupla_somada)

n1, n2, n3, *_ = tupla_4
print(n2)

tupla_multiplicada = (1, 2, 3, 4, 'Caio', 6) * 20
print(tupla_multiplicada)