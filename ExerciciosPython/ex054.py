'''
Projeto: Grupo da Maioridade
'''
from datetime import date
contador = 0
for ano in range(1,8):
    nascimento = int(input('Digite o ano em que você nasceu: '))
    if date.today().year - nascimento >= 21:
        contador += 1
print('{} pessoas já atingiram a maioridade!'.format(contador)) 