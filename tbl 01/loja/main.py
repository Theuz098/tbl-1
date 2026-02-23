
from carrinho import Produto, Carrinho
from pagamento import Pagamento

def main():
    
    produto1 = Produto("Camisa", 50.0)
    produto2 = Produto("Calça", 120.0)

    carrinho = Carrinho()
    carrinho.adicionar_produto(produto1, 2)
    carrinho.adicionar_produto(produto2, 1)
    total = carrinho.calcular_total()
    print(f"\nTotal do carrinho: R$ {total:.2f}\n")

    pagamento = Pagamento("Cartão de Crédito")
    pagamento.processar(total)

if __name__ == "__main__":
    main()