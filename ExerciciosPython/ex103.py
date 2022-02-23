"""
Projeto: Funcao jogador
"""
name = input('Digite o nome do jagador: ')
goals = input('Digite o número de gols: ')

if name.isalpha() == False:
    name = "<desconhecido>"
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

def Player(playerName = "<desconhecido>", numberGoals = 0):
    return f'O jogador {playerName} fez {numberGoals} gol(s) no campeonato'

print(Player(name, goals))