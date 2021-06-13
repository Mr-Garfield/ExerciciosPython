'''
Projeto: soma de pares
'''
somador = 0
for c in range(1, 7):
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        somador = somador + n
print(somador)