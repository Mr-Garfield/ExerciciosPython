"""
Projeto: Análise de números tupla
"""
numbers = (int(input('1º Número: ')), int(input('2º Número: ')),
           int(input('3º Número: ')), int(input('4º Número: ')))

print(f'Você digitou os valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)}x')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for par in numbers:
    if par % 2 == 0:
        print(par, end=' ')
