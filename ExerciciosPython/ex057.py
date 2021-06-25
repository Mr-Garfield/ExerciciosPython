'''
Projeto: Identificador de Gênero
'''
s = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while s not in 'MF':
    s = input('Tente novamente: [M/F] ').upper()
print('Sexo {} registrado!'.format(s))

 