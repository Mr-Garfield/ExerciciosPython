'''
Projeto: Comparador de valores
'''
a = float(input('Digite o 1° valor: '))
b = float(input('Digite o 2° valor: '))

if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')