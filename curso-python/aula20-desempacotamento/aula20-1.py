"""
Desempacotamento de listas em Python
"""
lista = ['Caio', 'Maria', 'João', 'Ju', 'Rafa']

n1, n2, *outra_lista, ultimo_da_lista = lista

print(n1, n2, outra_lista, ultimo_da_lista)
