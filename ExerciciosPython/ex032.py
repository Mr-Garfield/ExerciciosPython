'''
Projeto: Ano Bissexto
'''
from datetime import date

year = int(input('Digite um ano que deseja analizar: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano de {} é bixesto'.format(year))
else:
    print('O ano de {} não é bixessesto'.format(year))

