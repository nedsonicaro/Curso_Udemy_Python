"""
def boasvindas(saudacao, nome):
    print(f'{saudacao} {nome}')

boasvindas('Oi', 'icaro')
boasvindas('Olá', 'matheus')
boasvindas('Hello', 'pierre')
boasvindas('Hey', 'zeca')
"""

"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(2,3,4)
soma(50,100,300)
soma(34321,3151,800)
"""

"""
def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(100,50)
"""

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

print(fb(15))



