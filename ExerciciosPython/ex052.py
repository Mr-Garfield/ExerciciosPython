'''
Projeto: Indentificando número primo
'''

number = int(input('Digite um número inteiro para saber se ele é primo: '))

counter = 0

if number != 0 and number != 1:

    for primeNumber in range(1, number + 1):

        if number % primeNumber == 0:
            counter += 1

    if counter == 2:
        print('O número {} é PRIMO'.format(number))

    else:
        print('O número {} NÃO é PRIMO'.format(number))

else:
    print('O número 0 e 1 NÃO são considerados primos.'.format(number))