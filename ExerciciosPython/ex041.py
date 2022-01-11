'''
Projeto: Classificando atletas por idade
'''

from datetime import date

bornYear = int(input('Digite seu ano de nascimento: '))

category = ' '
years = date.today().year - bornYear

if years <= 9:
    category = 'MIRIN'
elif 9 < years <= 14:
    category = 'INFANTIL'
elif 14 < years <= 19:
    category = 'JUNIOR'
elif 19 < years <= 25:
    category = 'SÊNIOR'
else:
    category = 'MASTER'

print('O atleta possui {} anos.'.format(years))
print('Vai estar selecionado na categoria: {}'.format(category))