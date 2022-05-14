"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max,
range
"""
#  texto = 'Valor'
#  lista = [1, 2, 3, 4, 'Luiz Otávio', True]
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print('Lista: ', lista[1])
lista[5] = 'Qualquer outra coisa.'
print(lista[5])

#  fatiamento
print('Fatiamento: ', lista[0:3])
print('Fatiamento: ', lista[::2])
print('Fatiamento: ', lista[::-1])

string = 'ABCDE'
print('String: ', string[1])
print()

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
l1.extend('a')
l2.append('b')
l2.insert(0, 'c')
l2.pop()
l3 = l1 + l2

print(l1)
print(l2)
print(l3)
print()

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l4[3:5])
print(l4)
print()

print(max(l4))
print(min(l4))
print()

l5 = list(range(1, 10))
print(l5)
print()

soma = 0
for valor in l5:
    print('SOMA')
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')

print(soma)
print()

l6 = ['String', True, 10, -20.5]
for elem in l6:
    print(f'O tipo de {elem} é {type(elem)}')
print()
