class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)


# Execução do Primeiro Incremento
if __name__ == "__main__":
    

    p1 = Produto("Smartphone", 1800.0)
    p2 = Produto("Fone Bluetooth", 199.90)

    carrinho = Carrinho()
    carrinho.adicionar_produto(p1)
    carrinho.adicionar_produto(p2)

    print(f"Total do carrinho: R$ {carrinho.calcular_total():.2f}")