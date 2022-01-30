"""
Projeto: Matriz
"""
matriz = [[], [], [],
          [], [], [],
          [], [], [] ]

for values in range(0, 9):
    matriz[values].append(int(input(f'Digite um valor: ')))

for n, elements in enumerate(matriz):
    print(elements, end='')
    if n <= 2:
        print(f'[ {elements[0]} ]', end=' ')
        if n == 2:
            print()

    elif n <= 5:
        print(f'[ {elements[0]} ]', end=' ')
        if n == 5:
            print()
    else:
        print(f'[ {elements[0]} ]', end=' ')

