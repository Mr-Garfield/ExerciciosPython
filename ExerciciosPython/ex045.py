'''
Projeto: GAME - Pedra, papel e tesoura
'''

import random
from time import sleep

computer = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

print('-'*7)
print('Suas opções: ')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
print('-'*7)

move = int(input('Qual sua opção? '))

if move == 1 or move == 2 or move == 3:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print('-=--=' * 10)
    print('O computador escolheu {}'.format(computer))
    print('Jogador: ', end='')

    #Pedra
    if computer == 'Pedra':
        if move == 1:
            print('EMPATOU')

        elif move == 2:
            print('GANHOU')

        else:
            print('PERDEU')

    #Papel
    elif computer == 'Papel':
        if move == 1:
            print('PERDEU')

        elif move == 2:
            print('EMPATOU')

        else:
            print('GANHOU')

    #Tesoura
    else:
        if move == 1:
            print('GANHOU')

        elif move == 2:
            print('PERDEU')

        else:
            print('EMPATOU')
    print('-=--=' * 7)
else:
    print('Digite uma opção válida!')

