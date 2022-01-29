"""
Projeto: Lista ordenada sem repetições
"""

listNumbers = []

for n in range(0, 5):
    number = int(input('Digite um número: '))

    if number not in listNumbers:

        if n == 0 or number > listNumbers[-1]:
            listNumbers.append(number)

        else:
            for position in range(0, len(listNumbers)):  # corre todos os elementos da lista

                if number < listNumbers[position]:
                    listNumbers.insert(position, number)
                    break

print(listNumbers)


