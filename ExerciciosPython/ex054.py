'''
Projeto: Grupo da maioridade
'''

from datetime import date

counter = 0

for years in range(1, 8):
    bornYear = int(input('Ano de nascimento {}° pessoa: '.format(years)))

    if date.today().year - bornYear >= 18:
        counter += 1

print('{} pessoas já atigiram a maior idade!'.format(counter))
print('{} pessoas do grupo ainda são de menor!'.format(7 - counter))