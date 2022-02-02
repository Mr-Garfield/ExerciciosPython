"""
Projeto: Boletim com listas compostas
"""

studentGrade = []
counter = 0
while True:

    studentGrade.append(["", [float(), float()]])
    # Outra opção seria criar 3 variáveis e utilizar o append para colocar cada uma em sua posição.
    studentGrade[counter][0] = input('Nome: ')
    studentGrade[counter][1][0] = float(input('Nota1: '))
    studentGrade[counter][1][1] = float(input('Nota2: '))

    option = input('Deseja continuar? [S/N] ')

    if option in 'nN':
        break
    else:
        counter += 1

print(f'{"N°":<4} {"NOME":<7} {"MÉDIA":>8}')
print('---------------------')
for number, student in enumerate(studentGrade):
    print(f'{number:<5}', end='')
    print(f'{student[0]:<7}', end='')
    media = sum(student[1]) / 2
    print(f'{media:>8.1f}')
print('---------------------')

while True:
    number = int(input('Digite o número do aluno para ver suas notas: (000 para parar) '))
    if number == 000:
        break
    print(f'As notas de {studentGrade[number][0]} são {studentGrade[number][1]}')


