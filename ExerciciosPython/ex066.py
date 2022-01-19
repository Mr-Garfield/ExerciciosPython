"""
Projeto: Vários números e flag de parada
"""

number = 0
counter = 0
adder = 0

while True:
    number = int(input('Digite um número: [999 para PARAR] '))
    if number == 999:
        break
    else:
        counter += 1
        adder += number

print(f'Foram digitados {counter} números e soma entre eles é {adder}!')
