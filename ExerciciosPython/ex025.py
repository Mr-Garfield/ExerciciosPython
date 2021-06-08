'''
Projeto: Verfica se o nome tem 'Silva'
'''
n = input('Digite seu nome completo: ')
s = 'silva' in n.lower()
print('Seu nome tem Silva? {}'.format(s))