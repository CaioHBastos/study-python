"""
Entrada de dados do usuário
"""
#  nome = input("Qual o seu nome? ")
#  print(f'O usuário digitou: {nome} e tipo da variável é: {type(nome)}')

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = 2021 - int(idade)
print()
print(f'{nome} tem {idade} anos, nascido em {ano_nascimento}')
