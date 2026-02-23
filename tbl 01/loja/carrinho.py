

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade=1):
        self.itens.append((produto, quantidade))
        print(f"{quantidade}x {produto.nome} adicionados ao carrinho.")

    def calcular_total(self):
        total = sum(produto.preco * quantidade for produto, quantidade in self.itens)
        return total