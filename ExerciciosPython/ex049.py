'''
Projeto: Tabuada v.2.0
'''

number = int(input('Digite um número para ver sua tabuada: '))

print('-' * 15)

for multiplierNumber in range(1, 11, 1):
    print('{} x {:2} = {}'.format(number, multiplierNumber, number * multiplierNumber))

print('-' * 15)
