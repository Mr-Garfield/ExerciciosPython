'''
Projeto: Índice de Massa Corporal (IMC)
'''
print('-'*15)
print('CÁLCULO DO IMC')
print('-'*15)
h = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
IMC = p / (h)**2
status = ''

if IMC < 18.5:
    status = 'Abaixo do peso'
elif 18.5 <= IMC < 25:
    status = 'Peso ideal'
elif 25 <= IMC < 30:
    status = 'Sobrepeso'
elif 30 <= IMC < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print('O seu IMC é {:.2f} e seu estado é de: {}'.format(IMC, status))
