from classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32, 'Masculino')
cliente1.insere_endereco('BH', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()


cliente2 = Cliente('Maria', 55, 'Feminino')
cliente2.insere_endereco('Salvador', 'Bahia')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 19, 'Masculino')
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
