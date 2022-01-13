'''
Projeto: Analisaor completo
'''

groupAge = 0
ageOlderMan = 0
nameOlderMan = ''
womenAccountant = 0

for people in range(1, 5):
    print('=+=+=+=+= {}° PESSOA =+=+=+=+='.format(people))
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    gender = str(input('Gênero [M/F]: ')).strip().upper()

    groupAge += age

    if gender == 'M' and ageOlderMan == 0:
        ageOlderMan = age
        nameOlderMan = name

    if gender == 'M' and age > ageOlderMan:
        ageOlderMan = age
        nameOlderMan = name

    if gender == 'F' and age < 20:
        womenAccountant += 1

print('A média de idade do grupo é {:.1f} anos'.format(groupAge / 4))
print('O homem mais velho tem {} ano e se chama {}.'.format(ageOlderMan, nameOlderMan))
print('O grupo tem {} mulhere(s) com menos de 20 anos.'.format(womenAccountant))
