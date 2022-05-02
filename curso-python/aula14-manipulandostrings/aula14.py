"""
Manipulando Strings
- String indices
- Fatiamento de Strings [inicio:fim:passo]
- Funções built-in len, abs, type, print, etc...
"""
#  positivos
texto = 'Python s2'
print(texto[2])
print()

#  negativos
url = 'www.google.com.br/'
print(url[:-1])
print()

nova_string = texto[2:6]
print(nova_string)
print()

nova_string = texto[:6]
print(nova_string)
print()

nova_string = texto[7:]
print(nova_string)
print()

nova_string = texto[0:6:2]
print(nova_string)
