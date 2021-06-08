"""
Projeto: Mostrando dados de uma variável.
"""
entrada = input('Digite algo: ')
print('O tipo primitivo é: {}'.format(type(entrada)))
print('Só tem espaço? {}'.format(entrada.isspace()))
print('É um número? {}'.format(entrada.isnumeric()))
print('É alfabético? {}'.format(entrada.isalpha()))
print('É alfanunérico? {}'.format(entrada.isalnum()))
print('Está em maiúsculas ? {}'.format(entrada.isupper()))
print('Está em minúsculas? {}'.format(entrada.islower()))
print('Está capitalizada? {}'.format(entrada.istitle()))