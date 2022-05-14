"""
+ adição
- subtração
* multiplicação
/ divisão
// divisão por inteiro
** exponenciação
% resto da divisão
()
"""
print('Multiplicação * ', 10 * 10)
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 5)
print('Divisão / ', 10 / 2)


print('Multiplicação * ', 10 * '10')  # Aparece como número de repetição (10 vezes o 10)
print('Adição * ', 5 * '5')  # Concatenação (55)

print('Divisão inteira // ', 10 // 3)
print('Potenciação **', 10 ** 3)
print('Resto da divisão %', 10 % 9)

print('Precedência () ', 5 * (2 + 10))
