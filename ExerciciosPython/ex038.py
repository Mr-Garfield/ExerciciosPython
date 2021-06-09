'''
Projeto: Comparador de valores
'''
a = float(input('Digite o 1° valor: '))
b = float(input('Digite o 2° valor: '))

if a > b:
    print('O valor {} é maior que o valor {}'.format(a, b))
elif b > a:
    print('O valor {} é maior que o valor {}'.format(b, a))
else:
    print('Não existe valor maior, os dois são iguais.')