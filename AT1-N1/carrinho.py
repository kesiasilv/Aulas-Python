## carrinho 
import os

produtos = (
    {'id': 1, 'nome': 'notebook', 'preco': 2800},
    {'id': 2, 'nome': 'mouse', 'preco': 38.55},
    {'id': 3, 'nome': 'teclado', 'preco': 85.48},
    {'id': 4, 'nome': 'monitor', 'preco': 850.89},
)

carrinho = []

def exibirOpcoes():
    print('\n\n')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Exibir itens e o valor total')
    print('4 - Limpar carrinhp de compras')
    print('5 - Sair')

def exibirProdutos():
    for p in produtos:
        print('Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'], p['nome'], p['preco']))

opcao = '1'

os.system('cls')
print('Carrinho de Compras \n')

def obterNomeProduto(id):
    for p in produtos:
        if p['id'] == id:
            return p['nome'] 


while opcao != '5':
    exibirOpcoes()
    opcao = input('Digite a opção: ')
    
    if opcao == '1':
        exibirProdutos()
        id = int(input('Digite o id do produto: '))
        quantidade = int(input('Digite a quantidade: '))
        carrinho.append({'id': id, 'quantidade': quantidade})

    if opcao == '2':
        id = int(input('Digite o id do produto: '))
        temp = []
        for item in carrinho:
            if item['id'] != id:
                temp.append(item)

    if opcao == '3':
        print('\n\n')
        somatorio = 0
        for item in carrinho:
            for produto in produtos:
                if produto['id'] == item['id']:
                    somatorio = somatorio + (produto['preco'] * item['quantidade'])
                    break

            print('Nome: {0} - Quantidade: {1}'.format(obterNomeProduto(item['id']), item['quantidade']))
        print('Preço Total: {0}'.format(somatorio))
    
    if opcao == '4':
        carrinho = []
