'''
Projeto: Calculando a hipotenusa
'''

catetoA = float(input('Digite a mediada do cateto oposto: '))
catetoB = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = (catetoA ** 2 + catetoB ** 2) ** 0.5
print('A hipotenusa dos catetos digitados é: {:.2f}'.format(hipotenusa))

# Utilizadno a biblioteca math ficaria
'''
importh math
catetoA = float(input('Digite a mediada do cateto oposto: '))
catetoB = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = math.hypot(catetoA, catetoB)
print('A hipotenusa dos catetos digitados é: {:.2f}'.format(hipotenusa))
'''