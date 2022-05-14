"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
numero_1 = 10
numero_2 = 3
divisao = 10 / 3

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print()

nome = 'Caio Bastos'
print(f'{nome:s}')
print()

num_1 = 1
print(f'{num_1:0>10}')
print()

num_2 = 1150
print(f'{num_2:0<10}')
print()

num_2 = 1150
print(f'{num_2:0^10}')
print()

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = ' Caio Bastos '
print((50-len(nome)) / 2)
print()

print(f'{nome:#^50}')
print()

nome = 'Caio'
sobrenome = 'Bastos'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

