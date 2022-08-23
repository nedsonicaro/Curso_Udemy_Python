from map import produtos, pessoas, lista

"""
nova_lista = map(lambda x: x * 2, lista)
print(lista)
print(list(nova_lista))
"""

"""
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
"""
"""
nomes = map(lambda p: p['idade'], pessoas)

for pessoa in nomes:
    print(pessoa)
"""
nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))