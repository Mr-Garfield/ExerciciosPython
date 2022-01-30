"""
Projeto: Sublistas pares e ímpares
"""
listNumbers = [[], []]

for counter in range(0, 7):
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        listNumbers[0].append(number)
    else:
        listNumbers[1].append(number)

listNumbers[0].sort()
listNumbers[1].sort()
print(f'Os valores pares digitados foram: {listNumbers[0]}')
print(f'Os valores ímpares digitados foram: {listNumbers[1]}')
