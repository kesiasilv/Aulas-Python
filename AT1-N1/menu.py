# menu de opçoes
def exibirMenu():
    print("== SISTEMA DE LOJA ==\n")
    print("1. Adicionar itens")
    print("2. excluir item")
    print("3. Vizualizar itens")
    print("4. Sair")

def adicionarItem(lista):
    item = input("\nDigite o item a ser adicionado: ")
    quantidade = int(input("\nDigite a quantidade: "))
    lista.append(f"{item} (Quantidade: {quantidade})")
    print(f"\nO item '{item}' foi cadastrado com sucesso!")

def vizualizarItens(lista):
    if not lista:
        print("\nA lista de compras está vazia.")
    else:
        print("\nLista de Compras:")
        for item in range(len(lista)):
            print(f"- {item}: {lista[item]}")

def removerItem(lista):
    vizualizarItens(lista)
    if lista:
        itemParaRemover = int(input("\nDigite o código do item que deseja remover: "))
        itemRemovido = lista.pop(itemParaRemover)
        print(f"\nO item '{itemRemovido}' foi removido com sucesso.")

def executarPrograma():
    continuar = True
    listaCompras = []

    while continuar:

        exibirMenu()

        escolha = input("\nEscolha uma opção do Menu: ")

        if escolha == "1":
            adicionarItem(listaCompras)
        elif escolha == "2":
            removerItem(listaCompras)
        elif escolha == "3":
            vizualizarItens(listaCompras)
        elif escolha == "4":
            continuar = False
            print("programa finaizado.")
        else:
            print("\nOpção invalida, Por favor tente novamente.")


executarPrograma()
