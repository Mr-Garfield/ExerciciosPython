'''
Projeto: Maior e menor valores
'''

value1 = int(input('Digite o primeiro valor: '))
value2 = int(input('Digite o segundo valor: '))
value3 = int(input('Digite o terceiro valor: '))

# Verifica qual o menor valor
if value1 <= value2 and value1 <= value3:
    lowerValue = value1
elif value2 <= value1 and value2 <= value3:
    lowerValue = value2
else:
    lowerValue = value3
print('O menor valor é: {}'.format(lowerValue))

# Verifica qual o maior valor
if value1 >= value2 and value1 >= value3:
    highestValue = value1
elif value2 >= value1 and value2 >= value3:
    highestValue = value2
else:
    highestValue = value3
print('O maior valor é: {}'.format(highestValue))


