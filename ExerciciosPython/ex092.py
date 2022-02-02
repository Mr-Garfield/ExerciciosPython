"""
Projeto: Carteira de trabalho
"""

from datetime import date
# Carteira de trabalho e previdência social
workCard = dict()

workCard['name'] = input('Nome: ')
bornYear = int(input('Ano de nascimento: '))
workCard['age'] = date.today().year - bornYear
workCard['ctps'] = int(input('N° Carteira de Trabalho (0 não tem): '))

if workCard['ctps'] != 0:
    workCard['hiring'] = int(input('Ano de contratação: '))
    retirement = 35 - (date.today().year - workCard['hiring'])
    workCard['salary'] = float(input('Salário: R$ '))

    print("=+="*5)

    print(f'Nome: {workCard["name"]}')
    print(f'Idade: {workCard["age"]}')
    print(f'Número CTPS: {workCard["ctps"]}')
    print(f'Você foi contratado em: {workCard["hiring"]}')
    print(f'Salário tem o valor de R$ {workCard["salary"]:.2f}')
    print(f'Você vai se aponsentar com {workCard["age"] + retirement} anos')

else:
    print("=+="*5)
    print('Você não possui carteira de trabalho.')



