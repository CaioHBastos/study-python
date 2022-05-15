"""
Funções - def em Python
"""


def saudacao(mensagem='Olá', nome='usuário'):
    mensagem = mensagem.lower()
    nome = nome.upper()
    #  print(mensagem, nome)
    return f'{mensagem} {nome}'


variavel = saudacao()
print(variavel)

#  saudacao('Salve', 'Caio Bastos')
#  saudacao('Hello')
#  saudacao(nome='Caio')
#  saudacao(nome='Caio', mensagem='Hi')
