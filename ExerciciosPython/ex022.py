'''
Projeto: Analizador de Textos
'''

name = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é: {}'.format(name.upper()))
print('Seu nome em minúsculas é: {}'.format(name.lower()))
print('Seu nome ao todo tem {} letras'.format(len(name) - name.count(' ')))
nameSeparation = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nameSeparation[0], len(nameSeparation[0])))