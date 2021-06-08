'''
Projeto: Jogo da Adivinhação v.1.0
'''
from random import randint
from time import sleep

print('~=~'*25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('~=~'*25)
number = int(input('Em qual número eu pensei? '))
drawnNumber = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if drawnNumber == number:
    print('Você venceu :) !!! eu pensei em {}'.format(drawnNumber))
else:
    print('Você perdeu :( ... Eu pensei em {} e você digitou {}.'.format(drawnNumber, number))

