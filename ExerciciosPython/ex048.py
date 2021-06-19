'''
Projeto: Soma de ímpares múltiplos de 3
'''
soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador += 1
        soma += n
print('A dos {} ímpares múltipos de 3 vale {}'.format(contador, soma))