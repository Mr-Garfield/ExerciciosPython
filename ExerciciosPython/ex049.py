'''
Projeto: Tabuada v2.0
'''
n = int(input('Digite um número para ver sua tabuada: '))

for t in range(1,11):
    tabuada = n * t
    print('{} x {} = {}'.format(n, t, tabuada))