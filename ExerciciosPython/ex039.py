'''
Projeto: Alistamento Militar
'''
from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade <= 17:
    print('Você não precisa se alistar agora, ainda faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Já está na idade de se alistar. AVANTE SOLDADO!!!')
else:
    print('CORRA PARA SE ALISTAR!!! Você já têm {} anos, passou {} anos do prazo.'.format(idade, idade - 18))
