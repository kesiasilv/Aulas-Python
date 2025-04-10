import loja
import carrinho

def exibir_menu():
    print("\n== MENU LOJA VIRTUAL ==")
    print("1. Listar produtos")
    print("2. Adicionar produto ao carrinho")
    print("3. Remover produto do carrinho")
    print("4. Visualizar carrinho")
    print("5. Aplicar desconto a um produto")
    print("6. Finalizar compra")
    print("7. Sair")

def main():
    loja = Loja()
    carrinho = Carrinho()
    executando = True

    while executando:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.exibir_produtos()

        elif opcao == "2":
            loja.exibir_produtos()
            try:
                indice = int(input("Digite o número do produto: "))
                quantidade = int(input("Digite a quantidade: "))
                produto = loja.encontrar_produto(indice)
                if produto:
                    carrinho.adicionar(produto, quantidade)
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "3":
            carrinho.exibir_itens()
            nome = input("Digite o nome do produto para remover: ")
            carrinho.remover(nome)

        elif opcao == "4":
            carrinho.exibir_itens()

        elif opcao == "5":
            loja.exibir_produtos()
            try:
                indice = int(input("Digite o número do produto para aplicar desconto: "))
                percentual = float(input("Digite o percentual de desconto (%): "))
                loja.aplicar_desconto_produto(indice, percentual)
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "6":
            carrinho.exibir_itens()
            total = carrinho.calcular_total()
            if total > 0:
                sucesso = loja.processar_pagamento(total)
                if sucesso:
                    carrinho.esvaziar()
            else:
                print("Carrinho vazio.")

        elif opcao == "7":
            executando = False
            print("Saindo da loja. Até mais!")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
