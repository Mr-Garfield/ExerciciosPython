"""
Projeto: Cadastro jogador de futebol
"""

footballPlayer = dict()

footballPlayer['nome'] = input('Nome do jogador: ')
footballPlayer['partidas'] = int(input('Números de partidas jogadas: '))

print('Número de gols: ')
numbersGoals = list()
for n in range(1, footballPlayer['partidas']+1):
    goals = int(input(f'{n}° jogo: '))
    numbersGoals.append(goals)
print('=+='*12)

footballPlayer['gols'] = numbersGoals
footballPlayer['total'] = sum(numbersGoals)

for n, v in footballPlayer.items():
    print(f'O campo {n} tem valor de {v}')

print('=+='*12)

print(f'O jogador {footballPlayer["nome"]} jogou {footballPlayer["partidas"]} partidas')

for n, p in enumerate(footballPlayer['gols']):
    print(f'   → Na partida {n+1}, fez {p} gols')

