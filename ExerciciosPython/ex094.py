"""
Projeto: Unindo dicionários e listas
"""

person = dict()
people = list()

while True:
    person['nome'] = input('Nome: ')
    person['idade'] = int(input('Idade: '))
    person['genero'] = input('Gênero: [M/F] ').upper().strip()
    people.append(person.copy())
    option = input('Deseja continuar? [S/N] ').strip()
    if option in 'nN':
        break

print(people)

print('=+='*13)
averageAge = 0
numberPeople = len(people)
for age in people:
    averageAge += age['idade']


print(f'O grupo tem {numberPeople} pessoas')
print(f'A média de idade do grupo é {averageAge / numberPeople:.1f}')
print(f'As mulheres cadastradas foram: ', end=' ')
for women in people:
    if women['genero'] == 'F':
        print(women['nome'], end=' ')

print('\nAs pessoas com idade a cima da média são: ')
for aboveAverage in people:
    if aboveAverage['idade'] > averageAge / numberPeople:
        print(f'\nnome = {aboveAverage["nome"]}; gênero = {aboveAverage["genero"]}; idade = {aboveAverage["idade"]}')





