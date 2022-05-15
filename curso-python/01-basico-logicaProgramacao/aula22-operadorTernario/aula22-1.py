"""
Operador ternário em Python
"""
logger_user = True
msg = 'Usuário logado.' if logger_user else 'Usuário precisa logar.'

print(msg)
print()

idade = 18
e_de_maior = (idade >= 18)
msg_2 = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'

print(msg_2)
