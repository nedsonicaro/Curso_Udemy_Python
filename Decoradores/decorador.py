"""
def master(funcao):
    def slave():
        funcao()
    return slave

def fala_oi():
    print('Oi')

variavel = master(fala_oi)
variavel()
"""

def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend((clientes_iteravel))
    return lista


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)