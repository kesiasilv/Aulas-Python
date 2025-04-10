class Carrinho:
    def __init__(self):
        self.itens = []  # cada item será um dicionário com 'produto' e 'quantidade'

    def adicionar(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.itens.append({'produto': produto, 'quantidade': quantidade})
            produto.estoque -= quantidade
            print(f"{quantidade}x {produto.nome} adicionado ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.nome}.")

    def remover(self, nome_produto):
        for item in self.itens:
            if item['produto'].nome.lower() == nome_produto.lower():
                item['produto'].estoque += item['quantidade']
                self.itens.remove(item)
                print(f"{item['quantidade']}x {item['produto'].nome} removido do carrinho.")
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
        print("Carrinho esvaziado.")
