'''
Projeto: Calculando aluguel de carro
'''
d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
v = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(v))