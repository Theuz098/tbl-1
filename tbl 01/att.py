from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.data = datetime.now()
        self.cliente = cliente
        self.produtos = []

    # adiciona produto na lista
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    # calcula o valor total do pedido
    def calcular_total(self):
        total = 0
        for p in self.produtos:
            total = total + p.preco
        return total

    # informações do pedido
    def mostrar_pedido(self):
        print("===== PEDIDO =====")
        print("Numero:", self.numero)
        print("Data:", self.data)
        print("Cliente:", self.cliente.nome)
        print("Produtos:")

        for p in self.produtos:
            print("-", p.nome, "- R$", p.preco)

        print("Total: R$", self.calcular_total())


# TESTE DO SISTEMA


cliente1 = Cliente("João Silva", "12345678900", "joao@email.com")

produto1 = Produto("Notebook", 3500)
produto2 = Produto("Mouse", 150)

pedido1 = Pedido(1, cliente1)

pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)

pedido1.mostrar_pedido()
