'''
Projeto: Jogo da adivinhação v.2.0
'''

from random import randint

print('=+='*10)
print('DIGITE UM NÚMERO ENTRE 1 E 10')
print('=+='*10)

numberCoputer = randint(1, 11)
numberPlayer = input('Em qual número eu pensei? ')
counter = 1

while numberCoputer != numberPlayer:
    numberPlayer = int(input('Não foi esse número que eu pensei, tente novamente: '))
    counter += 1
print('Parabéns! O númeo que eu pensei foi {} foi acertou em {} tentativas.'.format(numberCoputer, counter))
