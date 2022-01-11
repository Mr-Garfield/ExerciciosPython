'''
Projeto: Gerenciador de pagamentos
'''

print('-=--='*5, 'MERCEARIA LOURENÇO', '-=--='*5)

purchaseValue = float(input('Preço das compras: R$'))

print('Formas de Pagamento: ')
print('-'*10)
print('[1] à vista dinheiro\cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
print('-'*10)
formPayment = int(input('Selcione uma opção: '))

if formPayment == 1:
    print('Pagando avista no dinheiro\cheque sua compra fica no valor de: R${:.2f}'.format(purchaseValue))

elif formPayment == 2:
    discount = purchaseValue - (purchaseValue * 0.05)
    print('À vista no cartão você recebe um disconto de 5% e vai pagar: R${:.2f}'.format(discount))

elif formPayment == 3:
    print('Você vai pagar 2 parcelas de: R${:.2f}'.format(purchaseValue / 2))

elif formPayment == 4:
    purchaseInterest = purchaseValue + (purchaseValue * 0.10)
    numberInstallments = int(input('Digite o número de vezes em que deseja pagar: '))
    installmentsValue = purchaseInterest / numberInstallments
    print('Parcelando {}x você irá pagar um juros de 20% e vai pagar parcelas de: R${:.2f}'.format(numberInstallments, installmentsValue))

else:
    print('Digite uma opção válida!')

