'''
Projeto: Analisando triângulos v.2.0

Equilátero: Todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: Todos os lados diferentes

'''

line1 = float(input('Primeiro segmento: '))
line2 = float(input('Segundo segmento: '))
line3 = float(input('Terceiro segmento: '))

if line1 + line2 > line3 and line1 + line3 > line2 and line2 + line3 > line1:

    if line1 == line2 == line3:
        triangle = 'EQUILÁTERO'

    elif line1 == line2 or line1 == line3 or line2 == line3:
        triangle = 'ISÓCELES'

    else:
        triangle = 'ESCALENO'

    print('Os segmentos formam um triângulo: {}'.format(triangle))

else:
    print('Os segmentos NÃO podem formar um triângulo.')
