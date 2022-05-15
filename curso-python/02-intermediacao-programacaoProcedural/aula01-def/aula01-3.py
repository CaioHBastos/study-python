"""
Funções (def) em Python - *args **Kwargs*
"""

"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a2, a2, a3, a4, a5, nome, a6)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='Caio', a6=5)
print(var[0], var[1])
"""


def func(*args):
    print(args)
    for valores in args:
        print(valores)


lista = [1, 2, 3, 4, 5]
func(*lista)


def func_1(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')

    if idade:
        print(idade)
    else:
        print('Idade não informada')


lista = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]
func_1(*lista, *lista_2, nome='Caio', sobrenome='Bastos')
