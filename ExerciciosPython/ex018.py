'''
Projeto: Calculando Sen, Cos e Tan de um ângulo
'''
from math import sin, cos, tan, radians

a = float(input('Digite um ângulo que você deseja: '))
a = radians(a) # Converte de angulo para radianos

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(a, sin(a)))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(a, cos(a)))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(a, tan(a)))

