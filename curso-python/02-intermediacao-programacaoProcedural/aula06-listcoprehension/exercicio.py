"""
Separar em grupos de 0-9 com list comprehension
"""
string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10

lista = [string[i: i + n] for i in range(0, len(string), n)]
print(lista)

retorno = '.'.join(lista)
print(retorno)
