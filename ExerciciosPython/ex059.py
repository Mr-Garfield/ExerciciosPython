'''
Projeto: Criando um menu de opções
'''

option = None
mathOperation = None

while option != 5:

    number1 = int(input('Primeiro número: '))
    number2 = int(input('Segundo número: '))

    print('-'*10)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print('-'*10)

    option = int(input('Ecolha uma opção: '))

    if option == 1:
        mathOperation = number1 + number2
        print('{} + {} = {}'.format(number1, number2, mathOperation))

    elif option == 2:
        mathOperation = number1 * number2
        print('{} x {} = {}'.format(number1, number2, mathOperation))

    elif option == 3:
        if number1 > number2:
            print('O maior número é: {}'.format(number1))
        else:
            print('O maior número é: {}'.format(number2))

    elif option == 4:
        ...

    elif option == 5:
        break

    else:
        print('Ecolha uma opção válida: ')

print('Programa finalizado!')