'''
Projeto: Calculando desconto de 5%
'''
p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 0.05)
print('O produto que custava R${}, na promoção com de 5% vai custar R${:.2f}'.format(p, d))

