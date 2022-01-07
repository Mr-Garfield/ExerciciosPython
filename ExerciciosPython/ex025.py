'''
Projeto: Procurando uma string dentro de outra
'''

name = str(input('Qual seu nome completo? ')).lower().strip()
print('Seu nome tem Silva? {}'.format('silva' in name))