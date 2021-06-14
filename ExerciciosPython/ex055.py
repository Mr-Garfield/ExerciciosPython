'''
Projeto: Maior e Menor Peso 
'''
novaMassa = 0
menorMassa =0
maiorMassa = 0
for p in range(1,6):
    massa = float(input('Digite sua massa corporal: '))
    novaMassa = massa
    if massa > novaMassa:
        maiorMassa = massa
    elif massa < novaMassa:
        menorMassa = massa
    print('A maior massa corporal é {} e a menor {}'.format(maiorMassa, menorMassa))