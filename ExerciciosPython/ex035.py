'''
Projeto: Analizando triângulo v.1
'''
s1 = float(input('Digite o 1° segmento: '))
s2 = float(input('Digite o 2° segmento: '))
s3 = float(input('Digite o 3° segmento: '))

if (s1 + s2) > s3 and (s2 + s3) > s1:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos abaixo NÃO podem formar um triângulo.')
