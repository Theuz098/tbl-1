from carrinho import Produto, Carrinho


class Pagamento:
    def __init__(self, tipo):
        self.tipo = tipo

    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R$ {valor:.2f} via {self.tipo}...")
        print("Pagamento realizado com sucesso!")


# Execução do Segundo Incremento
if __name__ == "__main__":
   

    # Criando novamente os objetos para integrar com o carrinho
    p1 = Produto("Smartphone", 1800.0)
    p2 = Produto("Fone Bluetooth", 199.90)

    carrinho = Carrinho()
    carrinho.adicionar_produto(p1)
    carrinho.adicionar_produto(p2)

    total = carrinho.calcular_total()

    pagamento = Pagamento("Pix")
    pagamento.processar_pagamento(total)