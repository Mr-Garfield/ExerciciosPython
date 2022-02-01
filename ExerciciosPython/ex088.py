"""
Projeto:
"""

from random import randint
from time import sleep

print('=+='*15)
print(f'{"JOGO DA MEGA SENA":^45}')
print('=+='*15)

numberGames = int(input('Quantos jogos você deseja sortear ? '))

print('=+=  '*3, end='')
print(f'SORTEANDO {numberGames} JOGOS',end='')
print(' =+='*3)

matrizGames = [[]]*numberGames
counter = 0

for games in range(0, numberGames):

    while True:
        numberSorted = randint(1, 60)
        if numberSorted not in matrizGames[games]:
            matrizGames[games].append(numberSorted)
            counter += 1

        if counter == 6:
            counter = 0
            break

    matrizGames[games].sort()
    print(f'Jogo{games+1}: {matrizGames[games]}')
    sleep(0.5)
    matrizGames[games].clear()
