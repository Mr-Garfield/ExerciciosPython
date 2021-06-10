'''
Projeto: Classificando Atletas por Idade
'''
from datetime import  date

nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
categoria = ''
if idade <= 9:
    categoria = 'MIRIN'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JUNIOR'
elif idade == 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('O atleta competirá na categoria: {}'.format(categoria))