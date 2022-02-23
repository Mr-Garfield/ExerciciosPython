"""
Projeto: Funcao para validacao de valor numerico
"""

def leiaInt(msg):
    validacao = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            validacao = True
            return n
        else:
            print('ERRO! Digite um número válido.')
        if validacao == True:
            break


number = leiaInt('Digite um número: ')
print(f'Você digitou o número {number}')