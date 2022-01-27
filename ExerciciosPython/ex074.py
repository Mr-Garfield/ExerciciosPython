"""
Projeto: Maior e menor valores em tupla
"""
from random import  randint

# Solução da Aula

numbers = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Os números sorteados foram: ', end='')
for number in numbers:
    print(number, end=' ')

print(f'\nO MAIOR número sorteado foi: {max(numbers)}')
print(f'O MENOR número sorteado foi: {min(numbers)}')



# Minha Solução

"""

import random

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

counter = 0
biggerNumber = 0
smallerNumer = 0

print('Números sorteados: ', end=' ')

while counter <= 4:
    drawNumber = random.choice(numbers)
    print(drawNumber, end=' ')
    counter += 1

    if counter == 1:
        biggerNumber = drawNumber
        smallerNumer = drawNumber

    if drawNumber > biggerNumber:
        biggerNumber = drawNumber

    if drawNumber < smallerNumer:
        smallerNumer = drawNumber

print()
print(f'O MAIOR número sorteado foi: {biggerNumber}')
print(f'O MENOR número sorteado foi: {smallerNumer}')


"""