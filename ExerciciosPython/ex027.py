'''
Projeto: Mostra o primeiro e o último nome de uma pessoa
'''
name = input('Digite seu nome: ').split()

print('Muito prazer te conhecer!')
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {}'.format(name[-1]))
