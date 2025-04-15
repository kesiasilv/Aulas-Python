class Loja:
    def __init__(self):
        from produto import Produto  
        self.produtos = [
            Produto("Notebook", 2800.00, 5),
            Produto("Mouse", 38.55, 10),
            Produto("Teclado", 85.48, 8),
            Produto("Monitor", 850.89, 4),
            Produto("Carregador", 35.60, 15)
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

    def processar_pagamento(self, total):
        print(f"\n[ Preço das compras: R${total:.2f} ]")
        print("\n== Formas de Pagamento: ==")
        print("[1] à vista dinheiro/cheque (10% de desconto)")
        print("[2] à vista cartão (5% de desconto)")
        print("[3] 2x no cartão")
        print("[4] 3x ou mais no cartão (+20% de juros)")

        try:
            opcao = int(input('\n\tQual é a opção? '))
        except ValueError:
            print("Opção inválida. Pagamento cancelado.")
            return False

        if opcao == 1:
            total *= 0.90
        elif opcao == 2:
            total *= 0.95
        elif opcao == 3:
            parcela = total / 2
            print(f'\nSua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
        elif opcao == 4:
            total *= 1.20
            try:
                totalParcela = int(input('Quantas Parcelas? '))
                parcela = total / totalParcela
                print(f'\nSua compra será parcelada em {totalParcela}x de R${parcela:.2f} COM JUROS')
            except ValueError:
                print("\nNúmero de parcelas inválido.")
                return False
        else:
            print('Opção inválida. Tente novamente.')
            return False
        print(f"\n Total a pagar: R${total:.2f}")
        print("Compra finalizada com sucesso!\n")  
        return True
        
