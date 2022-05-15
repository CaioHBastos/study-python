import copy

"""
Dicionários em Python
"""
dicionario_1 = {'chave1': 'valor da chave'}
print(dicionario_1)
dicionario_1['nova_chave'] = 'Valor da nova chave'
print(dicionario_1)
print(dicionario_1['chave1'])
print()

dicionario_2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
print(dicionario_2)
print(dicionario_2['chave2'])

if dicionario_2.get('chave4') is not None:
    print(dicionario_2.get('chave4'))

dicionario_2.update({'chave1': 'novo valor'})
print(dicionario_2.get('chave1'))
print(dicionario_2)

print()


"""
Suportados por Tuplas

dicionario_suportado = {
    'str': 'Valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}
print(dicionario_suportado['naoExiste'])

if 'naoExiste' in d1:
    print(d1['naoExiste])
    
print('Oi')
"""

dicionario_suportado = {
    'chave1': 'Valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla',
}
print('str' in dicionario_suportado)
print('str' in dicionario_suportado.keys())
print('Valor' in dicionario_suportado.values())
print(len(dicionario_suportado))

for k in dicionario_suportado:
    print(k)
print()

for v in dicionario_suportado.values():
    print(v)
print()

for k in dicionario_suportado.items():
    print(k)
print()

for k in dicionario_suportado.items():
    print(k[0], k[1])
print()

for k, v in dicionario_suportado.items():
    print(k, v)
print()


clientes = {
    'cliente1': {
        'nome': 'Caio',
        'sobrenome': 'Bastos',
    },
    'cliente2': {
        'nome': 'Joao',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
print()

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Caio', 'Bastos']}
v = d1.copy()
v[1] = 'Caio'

print(d1)
print(v)
print(v == d1)

v = copy.deepcopy(d1)
v[1] = 'Caio'
v['d'][0] = 'Joaozinho'
print(d1)
print(v)
