"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""


def function_filha():
    return 'Olá mundo!'


def function_mestre(function):
    return function()


executada = function_mestre(function_filha)
print(executada)


