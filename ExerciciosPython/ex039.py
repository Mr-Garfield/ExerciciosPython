'''
Projeto: Alistamento Militar
'''

from datetime import date

bornyear = int(input('Ano de nascimento: '))

actuallyYear = date.today().year

if actuallyYear - bornyear < 18:
    print('Você NÃO precisa se alistar, seu ano de alistamento será: {}'.format(bornyear + 18))
elif actuallyYear -bornyear == 18:
    print('IMPORTANTE! Você deve se alistar este ano({})'.format(actuallyYear))
else:
    yearsLate = actuallyYear - (bornyear + 18)
    print('URGENTE! Você está {} anos atrasado, deveria ter se alistado em {}!'.format(yearsLate, bornyear + 18))