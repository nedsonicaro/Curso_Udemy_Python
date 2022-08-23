from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('João')
caneta = Caneta('BIC', 'Azul')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca, caneta.cor)
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()