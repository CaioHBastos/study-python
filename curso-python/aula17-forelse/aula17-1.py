"""
For / Else em Python
"""
variavel = ['Caio Bastos', 'Joãozinho', 'Maria']

for valor in variavel:
    print(valor)
    continue
    #  break
print()

for valor in variavel:
    if valor.lower().startswith('c'):
        print(f'Começa com C: {valor}')
    else:
        print(f'Não começa com C: {valor}')
print()

for valor in variavel:
    if valor.lower().startswith('c'):
        break
else:
    print('Não existe uma palavra que começa com "C".')
