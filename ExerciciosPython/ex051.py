'''
Projeto: Calculando os 10 primeiros termos de uma PA
'''

# an = a1 + (n - 1).r

print('-=--='*5)
print('10 PRIMEIROS TERMOS PA')
print('-=--='*5)

firstTerm = int(input('Digite o primeiro termo da PA: '))
reason = int(input('Digite a razão: '))

#calculando o último termo
an = firstTerm + (10 - 1) * reason

for numbers in range(firstTerm, an + 1, reason):
    print(numbers, end='..')