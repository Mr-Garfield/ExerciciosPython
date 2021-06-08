'''
Projeto: Calculando a hipotenusa
'''
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hip = (co ** 2 + ca ** 2) ** 0.5
hip = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))
