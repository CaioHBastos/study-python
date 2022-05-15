"""
Funções - def em Python
"""


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta inválida')


print()
"""
referenciando funcões
"""


def f(var):
    print(var)


def dumb():
    return f


variavel = dumb()
variavel('Pode imprimir algo na tela.')


"""
Conhecendo Tuplas - Lista que não pode ser alterada
"""


def dumb():
    return 'Caio', 'Bastos'


var = dumb()

print(var[1], type(var))
