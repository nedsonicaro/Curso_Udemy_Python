class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

        if self.preco == 0:
            print('O produto está de graça!')

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # Getter
    @property
    def preco(self):

        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('R$', '')
        self._preco = valor

p1 = Produto('BLUSA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 20)
p2.desconto(100)
print(p2.nome, p2.preco)