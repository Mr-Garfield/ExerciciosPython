"""
Projeto: Lista de preços com tupla
"""

print('=+='*15)
print(f'{"LISTA DE PREÇOS":^45}')
print('=+='*15)

list = ('Caderno', 10.00,
        'Lápis', 2.50,
        'Estojo', 5.00,
        'Borracha', 3.50,
        'Lapiseira', 7.00,
        'Grafite', 3.00,
        'Mochila', 250.00,
        'Tesoura', 5.00,
        'Notebook', 2500.00)

for items in range(0, len(list)):
    if items % 2 == 0:
        print(f'{list[items]:.<30}', end='')
    else:
        print(f'R${list[items]:>8.2f}')

print('=+='*15)
