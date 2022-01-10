'''
Projeto: Calculando média utilizando estruturas condicionais
'''

grade1 = float(input('Primeira nota: '))
grade2 = float(input('Segunda nota: '))

average = (grade1 + grade2) / 2

print('Sua média foi {:.2f}'.format(average))

if average < 5:
    print('Você está REPROVADO!')

elif 5 <= average <= 6.9:
    print('Estude mais, você está de RECUPERAÇÃO!')
else:
    print('Parabébs! Você foi APROVADO.')
