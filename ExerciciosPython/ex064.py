"""
Projeto: Tratando vários valores v.1.0
"""

number = None
#somador
adder = 0
counter = 0

while number != 999:
        number = int(input('Digite um número: [999 para sair] '))
        if number  != 999:
            adder += number
            counter += 1

print('Você digiou {} números e a soma entre eles é {}!'.format(counter, adder))
