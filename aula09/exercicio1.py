hora = input('Qual a hora atual? ')

if hora.isdigit():
    hora = int(hora)
else:
    print('Digite um HORÁRIO')

if (11 >= hora >= 0):
    print('Bom dia')
if (17 >= hora >= 12):
    print('Boa tarde')
if (23 >= hora >= 18):
    print('Boa noite')
if (hora > 23):
    print('Digite uma hora válida')