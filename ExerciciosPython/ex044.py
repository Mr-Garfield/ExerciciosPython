'''
Projeto: Gerenciador de pagamentos
'''
from time import sleep

value = float(input('Qual o valor do produto: R$'))
print('')
print('='*70)
print('                     MÉTODOS DE PAGAMENTOS')
print('='*70)
print('[1] - À vista Dinheiro / Cheque: 10% DESCONTO')
print('[2] - À vista Cartão: 5% DESCONTO')
print('[3] - 2x no Cartão sem juros')
print('[4] - A partir de 3x no Cartão, acrécimo de 20% do valor do produto.')
print('-'*70)
print('ESCOLHA UM DOS MÉTODOS DE PAGAMENTO ACIMA!')
metedo = int(input('DIGITE A OPÇÃO ESCOLHIDA: '))
print('PROCESSANDO...')
sleep(2)
print('')
if metedo == 1:
    desconto = value - value * 0.1
    print('O valor do produto é R${:.2f}, com desconto de 10% fica R${:.2f}! '.format(value, desconto))
elif metedo == 2:
    desconto = value - value * (5/100)
    print('O valor do produto é R${:.2f}, no catão avista e com 5% de desconto fica R${:.2f}!'.format(value, desconto))
elif metedo == 3:
    print('O valor do produto é R${:.2f}, em 2x sem juros fica 2 parcelas de R${:.2f}!'.format(value, value/2))
elif metedo == 4:
    juros = value + value * (20/100)
    print('O valor do produto é R${:.2f}, em 3x no cartão fica 3 parcelas de R${:.2f}!'.format(value, juros / 3))
else:
    print('Escolha uma opção válida!!')
print('')
print('BOAS COMPRAS, VOLTE SEMPRE S2!!!')

