"""
def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2

try:
    print(divide(10, 0))
except ValueError as error:
    print(error)
"""

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

numero = converte_numero(input('Digite um número '))

if numero is not None:
    print(numero * 5)
else:
    print('Isso não é um número.')