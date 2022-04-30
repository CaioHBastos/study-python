"""
Condições - IF, ELIF e ELSE - Operadores lógicos
and, or, not, in e not in
"""
#  (Verdadeiro E Verdadeiro) = Verdadeiro
#  (Verdadeiro E Falso) = Falso
#  comparacao1 and comparacao2

#  (Verdadeiro OR Falso) = Verdadeiro
#  comparacao1 or comparacao2

a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

nome = 'Luiz Otávio.'

if 'u' in nome:
    print("Existe a letra U no seu nome.")
else:
    print("Não existe.")

if 'ota' not in nome:
    print("Passou aqui.")
else:
    print("Não passou aqui.")


usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'caio'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print ('Usuário ou senha inválidos.')
