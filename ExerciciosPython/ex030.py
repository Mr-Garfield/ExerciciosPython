'''
Projeto: Informa se o número é par ou ímpar
'''

number = float(input('Digite um número para saber se é par ou ímpar: '))

if number % 2 == 0:
    print('O número {} é PAR'.format(number))
else:
    print('O número {} é ÍMPAR'.format(number))