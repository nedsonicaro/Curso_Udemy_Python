primeiro_nome = input('Digite o seu primeiro nome ')
tamanho = len(primeiro_nome)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
elif tamanho > 6:
    print('Seu nome é muito grande')