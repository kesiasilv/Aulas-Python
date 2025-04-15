class Carrinho:
    def __init__(self):
        self.itens = []  

    def adicionar(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.itens.append({'produto': produto, 'quantidade': quantidade})
        else:
            print(f"Estoque insuficiente para {produto.nome}.")

    def remover(self, nome_produto):
     for item in self.itens:
        if item['produto'].nome.lower() == nome_produto.lower():
            try:
                quantidade = int(input("Quantos deseja remover? "))
                if quantidade <= 0:
                    print("Quantidade inválida.")
                    return
                if quantidade >= item['quantidade']:
                    item['produto'].estoque += item['quantidade']
                    self.itens.remove(item)
                    print(f"Todos os itens de {nome_produto} foram removidos do carrinho.")
                else:
                    item['quantidade'] -= quantidade
                    item['produto'].estoque += quantidade
                    print(f"{quantidade}x {nome_produto} removido(s) do carrinho.")
                return
            except ValueError:
                print("Entrada inválida.")
                return
     print("Produto não encontrado no carrinho.")


    def calcular_total(self):
        return sum(item['produto'].preco * item['quantidade'] for item in self.itens)

    def exibir_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
        else:
            print("\nItens no carrinho:")
            for item in self.itens:
                p = item['produto']
                print(f"{item['quantidade']}x {p.nome} - R${p.preco:.2f}")
            print(f"Total: R${self.calcular_total():.2f}")

    def esvaziar(self):
        self.itens.clear()
        print("\n Carrinho esvaziado.\n")
