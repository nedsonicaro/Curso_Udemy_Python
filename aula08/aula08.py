nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80.0
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} KG.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')

if True:
    print("verdade")
else: print("Não é verdadeiro")

