'''
Projeto: Jogo da adivinhação v.1.0
'''

import random
import time

print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
numberUser = int(input('Em que número você pensou? '))
numberComputer = random.randint(0, 5)
print('PROCESSANDO...')
time.sleep(3)
if numberUser == numberComputer:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Que pena, você PERDEU :(')
print('O número que eu pensei foi: {}'.format(numberComputer))