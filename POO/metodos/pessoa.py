from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Icaro', 21)
print(p1.idade)
p1.get_ano_nascimento()
p1.por_ano_nascimento('Icaro', 2001)
print(p1)
print(p1.nome, p1.idade)
print(p1.gera_id())
