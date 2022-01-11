'''
Projeto: Ler 6 números e mostrar a soma apenas dos pares
'''

print('Digite 6 números para ver a soma dos pares: ')

sumEven = 0

for evenNumbers in range(1, 7):
    number = int(input('{}° número: '.format(evenNumbers)))
    if number % 2 == 0:
        sumEven += number
print('A soma dos números pares vale: {}'.format(sumEven))


