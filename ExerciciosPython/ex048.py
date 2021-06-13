'''
Projeto: Soma de ímpares múltiplos de 3
'''
soma = 0
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma = soma + n
        print(n)
print('A dos ímpares múltipos de 3 vale {}'.format(soma))