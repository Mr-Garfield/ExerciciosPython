"""
Projeto: Análise de dados lista composta
"""
person = list()
people = list()
weights = list()
while True:
    person.append(str(input('Nome: ')))
    person.append(float(input('Peso: ')))
    people.append(person[:])
    person.clear()
    user = input('Deseja continuar? [S/N] ').strip()

    if user in 'nN':
        break

for weight in people:
    weights.append(weight[1])

lessWeight = people[weights.index(min(weights))][1]
greaterWeight = people[weights.index(max(weights))][1]

print(f'Foram cadastradas {len(people)} pessoas')
print(f'O menor peso foi: {lessWeight}Kg. Que corresponde a(o) ',end='')
for p in people:
    if p[1] == lessWeight:
        print(f'[{p[0]}]', end='')
print(f'\nO maior peso foi: {greaterWeight}Kg. Que corresponde a(o) ',end='')
for p in people:
    if p[1] == greaterWeight:
        print(f'[{p[0]}]', end='')


