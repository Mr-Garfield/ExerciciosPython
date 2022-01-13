'''
Projeto: Maior e menor peso da sequência
'''

greaterWeight = 0
lessWeight = 0

for people in range(1, 6):
    weight = float(input('Peso {}° pessoa: '.format(people)))

    if weight > greaterWeight:
        greaterWeight = weight

    if people == 1:
        lessWeight = weight

    if weight < lessWeight:
        lessWeight = weight

print('O MENOR peso foi: {}Kg'.format(lessWeight))
print('O MAIOR peso foi: {}Kg'.format(greaterWeight))
