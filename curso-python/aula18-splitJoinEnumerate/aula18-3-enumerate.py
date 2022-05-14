"""
Split, Join, Enumerate em Python
* Split - Dividir uma string #  str
* Join - Juntar uma lista #  str
* Enumerate - Enumerar elementos da lista #  list
"""
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor_real in enumerate(lista):
    print(indice, valor_real)

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for v in lista:
    print(v)
    print(v[0], v[1])
    for v_v in v:
        print(v_v)

lista_2 = ['Caio', 'João', 'Maria']

n1, n2, n3 = lista_2

print(n2)
