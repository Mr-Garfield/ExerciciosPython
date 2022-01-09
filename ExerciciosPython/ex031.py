'''
Projeto: Custo de uma viagem
'''

distace = float(input('Digite a distância a ser pecorrida em km: '))

if distace <= 200:
    price = distace * 0.50
else:
    price = distace * 0.45
print('O preço da passagem é: R${:.2f}'.format(price))
print('Boa viagem!')