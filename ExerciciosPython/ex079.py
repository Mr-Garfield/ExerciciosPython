"""
Projeto: Lista sem repetir valores
"""

listNumbers = []

while True:
    number = int(input('Digite um valor: '))

    if number not in listNumbers:
        listNumbers.append(number)

    else:
        print('Valor duplicado.')

    user = input('Deseja continuar? [S/N] ').lower()

    if user == 'n':
        break

listNumbers.sort()

print(f'Os valores digitados são {listNumbers} ')