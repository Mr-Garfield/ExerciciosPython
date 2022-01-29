"""
Projeto: Dividindo lista em pares e ímpares
"""

listNumbers = []
pairNumbers = []
oddNumbers = []
counter = 0

while True:

    number = int(input('Digite um valor: '))

    listNumbers.append(number)

    if listNumbers[counter] not in pairNumbers or listNumbers[counter] not in oddNumbers:

        if listNumbers[counter] % 2 == 0:
            pairNumbers.append(listNumbers[counter])

        else:
            oddNumbers.append(listNumbers[counter])


    counter += 1

    option = input('Deseja continuar? [S/N] ').lower().strip()

    if option == 'n':
        break

listNumbers.sort()
pairNumbers.sort()
oddNumbers.sort()

print(f'A lista dos números digitado é: {listNumbers}')
print(f'Os valores pares digitados foram: {pairNumbers}')
print(f'Os valores ímpares digitados fora: {oddNumbers}')

