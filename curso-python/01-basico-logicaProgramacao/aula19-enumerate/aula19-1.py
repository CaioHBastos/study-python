"""
Enumerate - Enumerar elementos da lista #  list
"""
lista = [
    ['Edu', 'João', 'Maria'],
    ['Maria', 'Ju', 'Caio'],
    ['Ed', 'Rainane', 'Rafa'],
]

print(lista)
print(lista[2])
print(lista[1][2])
print()

enumerada = list(enumerate(lista))
print(enumerada)
print(enumerada[1][1])
print()

for v1, v2 in enumerate(lista, 53):
    print(v1, v2)
