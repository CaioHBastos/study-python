"""
3 - Cria uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex 10%). Retorne (return) o valor do primeiro número somado 
do aumento do mesmo.
"""


def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


print(aumento_percentual(100, 10))
print(aumento_percentual(50, 10))

