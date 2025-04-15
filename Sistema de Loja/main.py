import os
from loja import Loja
from carrinho import Carrinho

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

loja = Loja()
carrinho = Carrinho()

while True:
    limpar_tela()
    print("== MENU LOJA VIRTUAL ==")
    print("1. Listar produtos")
    print("2. Adicionar produto ao carrinho")
    print("3. Remover produto do carrinho")
    print("4. Visualizar carrinho")
    print("5. Finalizar compra")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        limpar_tela()
        loja.exibir_produtos()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "2":
        limpar_tela()
        loja.exibir_produtos()
        try:
            indice = int(input("Digite o número do produto: "))
            produto = loja.encontrar_produto(indice)
            if produto:
                quantidade = int(input("Digite a quantidade: "))
                if quantidade <= produto.estoque:
                    carrinho.adicionar(produto, quantidade)
                    produto.estoque -= quantidade
                    print(f"{quantidade}x {produto.nome} adicionado ao carrinho.")
                else:
                    print("Quantidade indisponível no estoque.")
            else:
                print("Produto não encontrado.")
        except ValueError:
            print("Entrada inválida.")
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "3":
        limpar_tela()
        carrinho.exibir_itens()
        try:
            nome = input("Digite o nome do produto que deseja remover: ")
            carrinho.remover(nome)
        except Exception as e:
            print("Erro:", e)
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "4":
        limpar_tela()
        carrinho.exibir_itens()
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "5":
        limpar_tela()
        carrinho.exibir_itens()
        total = carrinho.calcular_total()
        if total == 0:
            print("Carrinho vazio. Adicione itens antes de finalizar a compra.")
        else:
            if loja.processar_pagamento(total):
                carrinho.itens.clear()
                print("\n---------------------")
                print("| Carrinho esvaziado.|")
        input("\nPressione Enter para voltar ao menu...")

    elif opcao == "6":
        print("Saindo da loja... Volte sempre!")
        break

    else:
        print("Opção inválida.")
        input("\nPressione Enter para voltar ao menu...")


