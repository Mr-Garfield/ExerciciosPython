"""
Projeto: Jogo par ou impar
"""

from random import randint

print('=+='*6)
print('PAR OU ÍMPAR')
print('=+='*6)

victories = 0
losses = 0

while True:

    numberComputer = randint(1, 5)
    numberUser = int(input('Digite um número entre 0 e 5: '))
    option = str(input('Par ou Ímpar: [P/I] ')).strip().upper()
    print('-'*20)

    sum = numberComputer + numberUser
    result = sum % 2

    if option == 'P' and result == 0:
        print(f'Parabéns! eu pensei no número {numberComputer}.')
        print(f'{numberComputer} + {numberUser} = {sum} formando um número PAR!')
        victories += 1

    elif option == 'P' and result != 0:
        print(f'Você PERDEU! ')
        print(f'{numberComputer} + {numberUser} = {sum} resultando em um número ÍMPAR.')
        losses += 1

    elif option == 'I' and result != 0:
        print(f'Parabéns! eu pensei no número {numberComputer}.')
        print(f'{numberComputer} + {numberUser} = {sum} formando um número ÍMPAR!')
        victories += 1

    else:
        print(f'Você PERDEU! ')
        print(f'{numberComputer} + {numberUser} = {sum} resultando em um número PAR.')
        losses += 1

    print('-' * 20)

    if victories == 2:
        print(f'Parabéns! Você GANHOU de {victories} x {losses}.')
        break

    if losses == 2:
        print(f'Você PERDEU de {losses} x {victories}. Mais sorte na próxima!')
        break

