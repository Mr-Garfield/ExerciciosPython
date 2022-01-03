'''
Projeto: Conversor de moedas [03/01/2022]
'''

real = float(input('Quanto dinheiro deseja converter: R$'))

print('Com R${} você pode comprar US${:.2f}'.format(real, real / 5.68))