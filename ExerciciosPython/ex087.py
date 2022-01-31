"""
Projeto: Matriz melhorada
"""

# i,j → Linha e coluna

matriz = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
adder = 0
thirdColumnSum = 0

for i in range(0, 3):#Seleciona a linha
    for j in range(0, 3): # Seleciona a coluna
        matriz[i][j] = int(input(f'Digite o valor da posição [{i}, {j}] '))

        if matriz[i][j] % 2 == 0:
            adder += matriz[i][j]

        if j == 2:
            thirdColumnSum += matriz[i][j]


# Mostrar a matriz formatada
for i in range(0, 3):#Seleciona a linha
    for j in range(0, 3): # Seleciona a coluna
       print(f'[ {matriz[i][j]:^5} ]',end='')
    print()

print(f'A soma dos valores pares digitados é: {adder}')
print(f'A soma dos valores da terceira coluna é: {thirdColumnSum}')
print(f'O maior valor da segunda linha foi: {max(matriz[1])}')

print('FIM')