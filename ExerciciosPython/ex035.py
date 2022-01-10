'''
Projeto: Verifica se as retas digitadas podem formar um triângulo
'''

straight1 = int(input('Digite o primeiro segmento: '))
straight2 = int(input('Digite o segundo segmento: '))
straight3 = int(input('Digite o terceiro segmento: '))

if (straight1 + straight2) > straight3 and (straight1 + straight3) > straight2 and (straight2 + straight3) > straight1:
    print('As retas {}, {} e {} PODEM formar um triângulo'.format(straight1, straight2, straight3))
else:
    print('As retas {}, {} e {} NÃO PODEM formar um triângulo'.format(straight1, straight2, straight3))
