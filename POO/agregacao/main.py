from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('blusa', 60)
p3 = Produto('meia', 10)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)

carrinho.lista_produto()
print(carrinho.soma_total())