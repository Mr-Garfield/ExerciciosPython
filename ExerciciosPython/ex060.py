'''
Projeto: Cálculo do fatorial
'''

factorial = int(input('Digite um número para ver seu fatorial: '))
result = 1

print('{}! = '.format(factorial), end='')

while factorial != 1:
    result *= factorial
    print('{} x '.format(factorial), end='')
    factorial -= 1

print('1 = {}'.format(result))

