## Formas de pagamento com descontos:

print('{:=^40}'.format(' Loja Silva '))
preco = float(input('preço de compras: R$'))
print(''' Formas de Pagamento
[1] à vista dinheiro/cheque (10% de desconto)
[2] à vista cartão (5% de desconto)
[3] 2x no cartão
[4] 3x ou mais no cartão(+20% de juros)''')

opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:2} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totalParcela = int(input('Quantas Parcelas? '))
    parcela = total / totalParcela
    print('Sua compra será parcelada em {}x de R${:2} COM JUROS'.format(totalParcela, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
print('Sua conta de R${:2} vai custar R${:2} no final.'.format(preco, total))
