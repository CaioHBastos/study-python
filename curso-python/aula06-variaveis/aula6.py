"""
Iniciar com letra, pode conter números, seperar _, letras minúsculas
"""
nome = 'Caio'  # Operador de atribuição
idade = 24
altura = 1.70
e_maior = idade > 18
peso = 70
imc = peso / (altura ** 2)

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(e_maior, type(e_maior))

print(nome, 'tem', idade, 'de idade e seu imc é: ', imc)
