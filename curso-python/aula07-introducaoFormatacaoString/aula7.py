nome = 'Caio'
idade = 24
altura = 1.70
e_maior = idade > 18
peso = 70
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'de idade e seu imc é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} {0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{m} tem {n} anos e seu imc é {o:.2f}'.format(m=nome, n=idade, o=imc))
