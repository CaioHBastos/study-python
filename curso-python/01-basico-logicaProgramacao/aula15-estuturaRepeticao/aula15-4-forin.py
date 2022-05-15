"""
For in em Python
Iterando Strings com for
Função range(start=0, stop, step=1
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)
print()

for n, letra in enumerate(texto):
    print(n, letra)
print()

for numero in range(10):
    print(numero)
print()

for numero in range(5, 10, 2):
    print(numero)
print()

for numero in range(20, 10, -1):
    print(numero)
print()

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)


