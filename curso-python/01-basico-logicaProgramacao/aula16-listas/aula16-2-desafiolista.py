"""
PROGRAMA ABAIXO
"""

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Aaaah isso não vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUUL, aletra "{letra}" existe na palavra secreta.')
    else:
        print(f'Afffzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        print('Dica: "Tem cheiro no ar"')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'QUE LEGAL, VOCE GANHOU !!!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta estáa assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
