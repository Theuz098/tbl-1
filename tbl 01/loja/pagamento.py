class Pagamento:
    def __init__(self, tipo):
        self.tipo = tipo

    def processar(self, valor_total):
        print(f"Processando pagamento de R$ {valor_total:.2f} via {self.tipo}...")
        print("Pagamento aprovado!")