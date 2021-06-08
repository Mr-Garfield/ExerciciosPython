'''
Projeto: O número é Par ou Impar
'''
number = float(input('Digite um número qualquer: '))
if number % 2 == 0:
    print('{} é PAR'.format(number))
else:
    print('{:.0f} é ÍMPAR'.format(number))
