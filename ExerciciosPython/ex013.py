'''
Projeto: Reajuste salarial
'''

s = float(input('Digite o salário do funcionário: R$'))
reajuste = s + (s * 0.15)
print('Antes o funcionário ganhava R${:.2f}, com o reajuste salarial de 15% passa a ganhar R${:.2f}'.format(s, reajuste))