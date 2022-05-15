"""
Expressões Lambda (funções anônimas)
"""


def funcao(arg1, arg2):
    return arg1 * arg2


var = funcao(2, 2)
print(var)

resultado = lambda x, y: x * y
print(resultado(2, 2))


"""
Ordanação
"""
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

"""
Ordanação com função
"""


def func(item):
    return item[1]


lista.sort(key=func, reverse=True)
print(lista)


"""
Ordenação com Lambda
"""
lista.sort(key=lambda item: item[1])
print(lista)

print(sorted(lista, key=lambda i: i[0], reverse=True))
