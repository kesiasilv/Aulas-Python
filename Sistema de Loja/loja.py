class Loja:
    def __init__(self):
        from produto import Produto  # para evitar import circular se for usado no main
        self.produtos = [
            Produto("Notebook", 2800.00, 5),
            Produto("Mouse", 38.55, 10),
            Produto("Teclado", 85.48, 8),
            Produto("Monitor", 850.89, 4)
        ]

    def exibir_produtos(self):
        print("\nProdutos disponíveis:")
        for idx, produto in enumerate(self.produtos, start=1):
            print(f"{idx}. {produto}")

    def encontrar_produto(self, indice):
        if 0 < indice <= len(self.produtos):
            return self.produtos[indice - 1]
        else:
            return None

    def aplicar_desconto_produto(self, indice, percentual):
        produto = self.encontrar_produto(indice)
        if produto:
            produto.aplicar_desconto(percentual)
            print(f"Desconto de {percentual}% aplicado ao produto {produto.nome}.")
        else:
            print("Produto não encontrado.")

    def processar_pagamento(self, total):
        print("\nFormas de Pagamento:")
        print("[1] Dinheiro/Pix (10% de desconto)")
        print("[2] Cartão à vista (5% de desconto)")
        print("[3] Cartão parcelado (20% de acréscimo)")

        opcao = input("Escolha a opção de pagamento: ")

        if opcao == "1":
            total *= 0.90
            print("Pagamento à vista com 10% de desconto.")
        elif opcao == "2":
            total *= 0.95
            print("Pagamento no cartão com 5% de desconto.")
        elif opcao == "3":
            total *= 1.20
            print("Pagamento parcelado com 20% de juros.")
        else:
            print("Opção inválida. Considerando valor total sem desconto/juros.")

        print(f"Total a pagar: R${total:.2f}")
        valor_pago = float(input("Digite o valor pago: R$"))

        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento aprovado. Troco: R${troco:.2f}")
            return True
        else:
            print("Valor insuficiente. Pagamento não concluído.")
            return False
