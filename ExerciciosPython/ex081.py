"""
Projeto: Extraindo dados de uma lista
"""

listNumbers = []


while True:
    number = int(input('Digite um valor: '))

    listNumbers.append(number)

    option = input('Deseja continuar? [S/N] ').lower().strip()

    if option == 'n':
        break

listNumbers.sort(reverse=True)

print(f'A lista em ordem decrescente é {listNumbers}')
print(f'Foram digitados {len(listNumbers)} números na lista.')
if 5 in listNumbers:
    print(f'O valor 5 foi digitado e está na {listNumbers.index(5) + 1}ª posição.')
else:
    print('O valor 5 não foi digitado.')

