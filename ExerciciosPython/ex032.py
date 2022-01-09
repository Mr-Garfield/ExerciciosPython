'''
Projeto: Analisar se o ano digita é bissexto
Obs:
Para um ano ser BISSEXTO ele tem que ser divisível por 4 e não pode ser divisível por 100.
ou
Se poder ser divido por 400 é um ano BISSEXTO.
'''

from datetime import date

yearTyped = int(input('Que ano quer analizar? (Digite 0 para o ano atual) '))

if yearTyped == 0:
    yearTyped = date.today().year

if (yearTyped % 4 == 0 and yearTyped % 100 != 0) or yearTyped % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(yearTyped))
else:
    print('O ano de {} NÃO é BISSEXTO'.format(yearTyped))