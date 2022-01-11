'''
Projeto: Calculando Índice de Massa Corporal (IMC)
'''

heigh = float(input('Digite sua altura: '))
weight = float(input('Digite seu peso: '))

imc = weight / (heigh ** 2)

print('Seu IMC: {:.2f}'.format(imc))
print('Você está ', end='')

if imc < 18.5:
    print('Abaixo do Peso')

elif 18.5 <= imc < 25:
    print('no Peso Ideal')

elif 25 <= imc < 30:
    print('com Sobrepeso')

elif 30 <= imc <= 40:
    print('com Obsidade')

else:
    print('Obsidade Mórbida')