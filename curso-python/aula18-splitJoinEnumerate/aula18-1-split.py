"""
Split, Join, Enumerate em Python
* Split - Dividir uma string #  str
* Join - Juntar uma lista #  str
* Enumerate - Enumerar elementos da lista #  list
"""
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    #  print(f'A palavra "{valor}" apareceu "{lista_1.count(valor)}x" na frase.')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor.strip()

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x')
