"""
Projeto: Análise de dados do grupo
"""

print('=+='*14)
print('CADASTRO DA PESSOA'.center(42))
print('=+='*14)

adults = 0
men = 0
women = 0

while True:
    age = int(input('Idade: '))
    gender = str(input('Gênero: [M/F] ')).strip().upper()[0]

    if age > 18:
        adults += 1

    if gender == 'M':
        men += 1

    else:
        if age < 20:
            women += 1

    print('-'*20)
    stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    if stop == 'N':
        break

print(f'Número de pessoas maior de 18 anos: {adults}')
print(f'Foram cadastrados {men} homens.')
print(f'{women} mulhere possuem menos de  20 anos.')





