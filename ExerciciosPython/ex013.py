'''
Projeto: Calculando aumento de salário de 15%
'''
s = float(input('Qual o salário do funcionário? R$'))
a = s + (s * 0.15)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(s, a))
