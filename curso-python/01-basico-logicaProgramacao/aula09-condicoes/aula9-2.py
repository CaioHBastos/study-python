"""
Condições - IF, ELIF e ELSE - Operadores relacionais
== > >= < <= !=
"""
#  print(2 == 2)
#  print(2 == 1)
#  print()
#  print(2 > 1)
#  print(2 >= 1)
#  print()
#  print(2 < 1)
#  print(2 <= 1)
#  print()
#  print(2 != 1)

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade_menor <= idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')