"""
Projeto: Número por extenso
"""

numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numberUser = int(input('Digite um número entre 0 e 20: '))

    if numberUser < 0 or numberUser > 20:
        numberUser = int(input('Tente novemente: '))

    print(f'Você digitou o número: {numbers[numberUser]}')
