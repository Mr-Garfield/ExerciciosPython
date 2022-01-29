"""
Projeto: Mairo e menor valor da lista
"""

counter = 0
listNumbers = []

while True:
    number = int(input('Digite uma valor: '))
    listNumbers.append(number)
    counter += 1
    if counter == 5:
        break

print(f'O MENOR valor digitado foi {min(listNumbers)} e está na posição {listNumbers.index(min(listNumbers)) + 1}')
print(f'O MAIOR valor digitado foi {max(listNumbers)} e está na posição {listNumbers.index(max(listNumbers)) + 1}')

