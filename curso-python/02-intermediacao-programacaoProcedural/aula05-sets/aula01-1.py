"""
Add (Adiciona), update (Atualiza), clear, discard
Union | (une)
Intersection & (Todos os elementos presentes nos dois)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos
"""
s1 = {1, 2, 3, 4, 5}
print(s1)

for v in s1:
    print(v)

s2 = set()
s2.add(1)
s2.add(2)
s2.add((1, 2, 3, 'Caio'))
print(s2)

s2.discard((1, 2, 3, 'Caio'))
print(s2)

s2.update('a')
print(s2)

s3 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3, 4, 5, 6}
s5 = s3 | s4
print(s5)

s3 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3, 4, 5, 6}
s5 = s3 & s4
print(s5)

s3 = {1, 2, 3, 4, 5, 7}
s4 = {1, 2, 3, 4, 5, 6}
s5 = s3 - s4
print(s5)

s3 = {1, 2, 3, 4, 5, 7}
s4 = {1, 2, 3, 4, 5, 6}
s5 = s3 ^ s4
print(s5)
