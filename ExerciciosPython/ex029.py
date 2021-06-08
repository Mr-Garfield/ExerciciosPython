'''
Projeto: Radar eletrônico
'''
v = float(input('Qual a velociade atual do carro? '))
m = (v - 80) * 7

if v >= 80:
    print('MULTADO! Você execedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')
