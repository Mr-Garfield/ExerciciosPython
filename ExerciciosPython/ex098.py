"""
Projeto: Função contador
"""

from time import sleep


def Traco():
    print('=+=' * 12)

def Contador(start, end, jump):

    if jump == 0:
        jump = 1

    print(f'Contagem de {start} até {end} de {abs(jump)} em {abs(jump)}')

    if start < end:
        counter = start
        while counter <= end:
            print(f'{counter} ', end='')
            sleep(0.5)
            counter += jump
        print('FIM!')

    else:
        counter = start
        while counter >= end:
            print(f'{counter} ', end='')
            sleep(0.5)
            counter -= abs(jump)
        print('FIM!')


Traco()
Contador(1, 10, 1)
Traco()
Contador(10, 0, 2)
Traco()

print('Personalize a contagem: ')
start = int(input('Iníco: '))
end = int(input('Fim: '))
jump = int(input('Passo: '))
Contador(start, end, jump)








