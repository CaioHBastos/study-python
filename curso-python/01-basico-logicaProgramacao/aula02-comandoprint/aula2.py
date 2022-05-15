
print(123456)  # Refere-se a uma função e recebe argumento
print('Caio', 'Bastos')  # Com a virgula por padrão coloca espaço, eles são argumentos
print('Caio', 'Bastos', sep='-')  # Funçao com o sep que coloca o separado entre os nomes
print('Caio', 'Bastos', sep='-', end='')  # Com o end ele não pula linha usando as aspas vazia
print('Juliana', 'Andrade', sep='-')  # Com o end ele não pula linha usando as aspas vazia


"""
Mascarando o CPF: 070.289.050-20
"""
print('070', '289', '050', sep='.', end='-')
print('20')
