"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def function_filha(nome):
    return f'Oi {nome}'


def function_filho(nome, saudacao):
    return f'{saudacao} {nome}'


def function_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


executada_1 = function_mestre(function_filha, 'Caio')
executada_2 = function_mestre(function_filho, 'Caio', saudacao='Bom dia!')
print(executada_1)
print(executada_2)

