"""
Quantidade de caracteres - LEN
"""
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)
print()
print(usuario, qtd_caracteres, type(qtd_caracteres))
print()
if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado com sucesso.')
