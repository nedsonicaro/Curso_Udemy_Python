num_1 = input('Digite um número inteiro ')

if num_1.isdigit():
    num_1 = int(num_1)
else:
    print('Isso não é um número inteiro')

if (num_1 % 2 == 0):
    print('Seu número é par')
else:
    print('Seu número é ímpar')



