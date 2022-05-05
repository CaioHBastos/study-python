"""
While em Python
Utilizado para realizar ações enquanto uma condição for verdadeira
"""
numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1
print('Acabou')

numero = 10
while numero < 20:
    if numero == 13:
        numero = numero + 1
        continue

    print(numero)
    numero = numero + 1
print('Acabou')

numero = 20
while numero < 30:
    if numero == 23:
        numero = numero + 1
        break

    print(numero)
    numero = numero + 1
print('Acabou')


x = 0
while x < 10:

    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1

    x += 1
print('Acabou')

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Informe um operador válido.')
