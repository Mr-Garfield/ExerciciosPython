'''
Projeto: Progressao aritmetica v.3.0
'''

firstTerm = int(input('Primeiro termo: '))
reason = int(input('Razão da PA: '))

counter = 0

pa = firstTerm

while counter < 10:
    print(pa, ' -> ', end='')
    pa += reason
    counter += 1
print('PAUSA')

counter = 0
terms = None
numberTerms = 10

while terms != 0:
    terms = int(input('Quantos termos a mais você deseja ver? '))
    numberTerms += terms
    while counter < terms:
        print(pa, ' -> ', end='')
        pa += reason
        counter += 1
    counter = 0
    if terms != 0:
        print('PAUSA')

print('Porgressão finalizada! Foram mostrados {} termos.'.format(numberTerms))
