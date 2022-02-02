"""
Projeto: Jogo de dados utilizando dicionario
"""

from random import randint
from time import sleep

player = dict()

for n in range(0, 4):
    dado = randint(1, 6)
    player[f'Jogador{n+1}'] = dado

for p, n in player.items():
    print(f'O {p} tirou {n}')
    sleep(0.5)

print('Ranking dos jogadores: ')
counter = 0

for p in sorted(player, key=player.get):
    counter += 1
    print(f'{counter}° lugar: {p} com {player[p]}')
    sleep(0.5)


