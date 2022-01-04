'''
Projeto: Calculando seno, cosseno e tangente
'''

import math

angulo = float(input('Digite o ângulo desejado: '))
angulo = math.radians(angulo)
print('O angulo de {} tem: '.format(angulo))
print('Seno: {:.2f}'.format(math.sin(angulo)))
print('Cosseno: {:.2f}'.format(math.cos(angulo)))
print('Cosseno: {:.2f}'.format(math.tan(angulo)))
