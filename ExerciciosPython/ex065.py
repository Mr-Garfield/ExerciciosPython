"""
Projeto: Maior e menor valores - while
"""

number = int(input('Digite um número: '))
option = str(input('Quer continuar? [S/N] ')).strip().upper()

counter = 1
smallerNumber = biggerNumber = adder = number


while option != 'N':
    number = int(input('Digite um número: '))

    adder += number
    counter += 1

    if number > biggerNumber:
        biggerNumber = number
    if number < smallerNumber:
        smallerNumber = number

    option = str(input('Quer continuar? [S/N] ')).strip().upper()

average = adder / counter

print('Foram digitados {} números e média dos números é {:.2f}'.format(counter, average))
print('O maior número foi {} e o menor foi {}'.format(biggerNumber, smallerNumber))
