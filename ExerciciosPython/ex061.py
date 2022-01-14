'''
Projeto: Progressão aritmética com while
'''

# an = a1 + (n - 1).r

print('-=--='*5)
print('10 PRIMEIROS TERMOS PA')
print('-=--='*5)

firstTerm = int(input('Primeiro termo: '))
reason = int(input('Digite a razão: '))

an = firstTerm + (10 - 1) * reason

terms = firstTerm

while terms <= an:
    print('{} -> '.format(terms), end='')
    terms += reason
print('Fim')
