'''
Projeto: Analisando Triângulos v2.0
'''
print('-'*20)
print('TIPOS DE TRIÂNGULOS')
print('-'*20)
a = float(input('Digite a medida 1° segmento: '))
b = float(input('Digite a medida 2° segmento: '))
c = float(input('Digite a medida 3° segmento: '))
print('')
if a + b > c and b + c > a:

    if a == b == c:
        print('Os segmentos acima formam um triângulo EQUILÁTERO.')
    elif a == b != c or b == c != a or a == c != b:
        print('Os segmentos acima formam um triângulo ESCALENO.')
    elif a != b != c:
        print('Os segementos acima formam um triângulo ISÓSCELES.')

else:
    print('Os segmentos acima NÃO podem formar um triângulo.')
