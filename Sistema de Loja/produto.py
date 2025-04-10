class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} (Estoque: {self.estoque})"
