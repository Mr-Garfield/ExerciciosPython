'''
Projeto: Validação de dados
'''

gender = input('Qual seu gênero? [M/F] ').strip().upper()[0]

while gender != 'M' and gender != 'F':

    if gender != 'M' and gender != 'F':
        gender = input('Opção inválida, tente novamente: ')

print('Gênero {} registrado com sucesso!'.format(gender))