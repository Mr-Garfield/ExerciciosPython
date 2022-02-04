"""
Projeto: Função para descobrir o maior valor
"""

def Maior(*numbers):
    print('=+='*12)
    print('Analizando valores...')
    for number in numbers:
        print(number, end=' ')
    print(f'Foram informados {len(numbers)} valores.')
    print(f'O maior valor informado foi {max(numbers)}')

Maior(1, 2, 3, 4, 5, 6)