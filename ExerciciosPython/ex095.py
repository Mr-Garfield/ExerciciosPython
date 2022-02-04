"""
Projeto: Jogadores de futebol aprimorado
"""
footballPlayer = dict()
players = list()


while True:
    footballPlayer['nome'] = input('Nome do jogador: ')
    footballPlayer['partidas'] = int(input('Números de partidas jogadas: '))
    print('Número de gols: ')
    numbersGoals = list()
    for n in range(1, footballPlayer['partidas'] + 1):
        goals = int(input(f'{n}° jogo: '))
        numbersGoals.append(goals)
    footballPlayer['gols'] = numbersGoals

    players.append(footballPlayer.copy())

    option = input('Deseja continuar ? [S/N] ').strip()
    print('-'*30)

    if option in 'nN':
        break

print(f'{"N°":<4} {"NOME":<9} {"GOLS":<6} {"TOTAL":>14}')
print('=+='*13)
for n, player in enumerate(players):
    print(f'{n:<5}', end='')
    print(f'{player["nome"]:<10}', end='')
    print(f'{player["gols"]!s:<5s}', end='')
    print(f'{sum(player["gols"]):>10}')
print('=+='*13)

while True:
    dados = int(input('Mostrar dados de qual jogador ? '))
    if dados == 999:
        break

    if dados >= len(players) or dados <= len(players) and dados != 0:
        print(f'Não existe o jogador {dados}')
    else:
        print(f'Dados do jogador {players[dados]["nome"]}:')
        for n, g in enumerate(players[dados]['gols']):
            print(f'No jogo {n+1} fez {g} gols')


print(players)
print('=+=' * 15)

