'''
Projeto: Calcular desconto (5%)
'''

p = float(input('Digite o preço do produto: R$'))

d = p - (p * (5 / 100))

print('O produto antes custava R${}, com o desconto de 5% passa a custar R${:.2f}'.format(p, d))