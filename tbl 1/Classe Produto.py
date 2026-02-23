# Classe Produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Classe Cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


# Classe Pedido demonstrando as associações
class Pedido:
    def __init__(self, cliente):
        # Associação com Cliente
        self.cliente_do_pedido = cliente
        
        # Associação com múltiplos Produtos usando lista
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.preco
        return total

    def exibir_resumo(self):
        print("=== RESUMO DO PEDIDO ===")
        print(f"Cliente: {self.cliente_do_pedido.nome} (CPF: {self.cliente_do_pedido.cpf})")
        print("Itens Comprados:")

        for item in self.itens:
            print(f"- {item.nome}: R$ {item.preco:.2f}")

        print(f"Total a pagar: R$ {self.calcular_total():.2f}")
        print("========================")


# Testes
if __name__ == "__main__":
    # Criando pelo menos 1 cliente e 2 produtos
    cliente1 = Cliente("João Silva", "123.456.789-00")
    prod1 = Produto("Notebook", 3500.00)
    prod2 = Produto("Mouse sem fio", 120.50)

    # Criando o pedido e associando entidades
    pedido = Pedido(cliente1)
    pedido.adicionar_produto(prod1)
    pedido.adicionar_produto(prod2)

    # Validando o resumo e o total
    pedido.exibir_resumo()