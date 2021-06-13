'''
Projeto: Progressão Aritmética
'''
# an = a1 + (n - 1).r
a1 = float(input('Digite o primeiro termo da P.A: '))
r = float(input('Digite qual a razão da P.A: '))
print('')
print('Os 10 primeiros termos da P.A são: ', end='')
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(f'{an:.0f}; ', end='')