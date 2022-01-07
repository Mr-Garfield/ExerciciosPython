'''
Projeto: Primeiro e último nome de uma pessoa
'''

name = input('Digite seu nome completo: ').strip().split()
print('Muito prezer em te conhecer!')
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {}'.format(name[-1]))