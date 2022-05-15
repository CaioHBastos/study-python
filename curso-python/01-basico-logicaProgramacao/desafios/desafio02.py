"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número
é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número: ')

try:
    numero = int(numero)

    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é impar')
except:
    print('Não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horário descrito, exiba a saudação apropriada. 
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input("Qual um horario (0 - 23)? ")

try:
    hora = int(hora)

    if 0 <= hora <= 11:
        print('Bom dia 0-11')
    elif 12 <= hora <= 17:
        print('Boa tarde 12-17')
    elif 18 <= hora <= 23:
        print('Boa noite 18-23')
    else:
        print('O Horário deve estar entre 0 e 23')
except:
    print('Não é um horário válido, precisa ser um número inteiro.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva 
"Seu nome é curto"; se tiver 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva 
"Seu nome é muito grande".
"""
nome = input('Digite seu primeiro nome: ')
quantidade_letras = len(nome)

if quantidade_letras <= 4:
    print('Seu nome é curto.')
elif 5 <= quantidade_letras <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')


