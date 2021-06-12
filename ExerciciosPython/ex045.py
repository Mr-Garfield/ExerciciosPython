'''
Projeto: GAME - Pedra, Papel e Tesoura.
'''
import random
computador = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('-'*15)
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
print('-'*15)
empate = False
vitoria = False
derrota = False
opcao = int(input('QUAL SUA ESCOLHA: '))
if opcao == 1:
    if computador == 'Pedra':
        empate = True
        vitoria = False
        derrota = False
        #print('EMPATE, quero ver se consegue me vencer agora!')
    elif computador == 'Papel':
        empate = False
        vitoria = False
        derrota = True
        #print('HAHAHA! Eu ganhei')
    elif computador == 'Tesoura':
        empate = False
        vitoria = True
        derrota = False
        #print('VOCÊ GANHOU!!! Na próxima será diferente...')
elif opcao == 2:
    if computador == 'Pedra':
        empate = False
        vitoria = True
        derrota = False
    elif computador == 'Papel':
        empate = True
        vitoria = False
        derrota = False
    elif computador == 'Tesoura':
        empate = False
        vitoria = False
        derrota = True
elif opcao == 3:
    if computador == 'Pedra':
        empate = False
        vitoria = False
        derrota = True
    elif computador == 'Papel':
        empate = False
        vitoria = True
        derrota = False
    elif computador == 'Tesoura':
        empate = True
        vitoria = False
        derrota = False
else:
    print('Escolha uma opção válida.')
if empate == True:
    print('EMPATE, quero ver se consegue me vencer agora!')
elif vitoria == True:
    print('VOCÊ GANHOU!!! Na próxima será diferente...')
elif derrota == True:
    print('HAHAHA! Eu ganhei')