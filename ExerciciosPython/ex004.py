'''
Projeto: Dissecando uma variável
'''

entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}'.format(type(entrada)))
print('Só tem espaço: {}'.format(entrada.isspace()))
print('É número: {}'.format(entrada.isnumeric()))
print('É alfabético: {}'.format(entrada.isalpha()))
print('É alfanumérico: {}'.format(entrada.isalnum()))
print('Está em maiúsculas: {}'.format(entrada.isupper()))
print('Está em minusculas: {}'.format(entrada.islower()))
print('Está capitalizada: {}'.format(entrada.istitle()))
