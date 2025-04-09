#criar menu de opçoes

def exibirMenu():
    print("== SISTEMA DE LOJA ==\n")
    print("1. Adicionar itens")
    print("2. excluir item")
    print("3. Vizualizar itens")
    print("4. Sair")

def executarPrograma():
    continuar = True

    while continuar:
        escolha = input("\nEscolha uma opção do Menu: ")

        if escolha == "1":
            print("Adicionar item selecionado")
        elif escolha == "2":
            print("Qual item deseja excluir")
        elif escolha == "3":
            print("Lista de Itens:")
        elif escolha == "4":
            print("programa finaizado")
        else:
            print("Opção invalida")


exibir = exibirMenu()
executar = executarPrograma()