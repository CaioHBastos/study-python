from random import randint

"""
4 - Fizz Buzz - Se o parâmetro da função for divísivel por 2, retorn fizz,
se o parâmetro da função for divível pro 5, retorne buzz. Se o parâmetro da função for
divível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o 
número enviado.
"""


def fizz_buzz(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return f'FizzBuzz, {valor} é divísivel por 3 e 5'
    if valor % 5 == 0:
        return f'buzz, {valor} é divísivel por 5'
    if valor % 3 == 0:
        return f'fizz, {valor} é divísivel por 3'
    return valor


for numero in range(100):
    aleatorio = randint(0, 100)
    resultado = fizz_buzz(aleatorio)
    print(resultado)
