'''
Projeto: RAdar eletrônico
'''

carSpeed = float(input('Digite a velocidade do carro: '))
if carSpeed > 80:
    # Multa em 7 reais por quilômetro ultrapassado
    print('Você foi multado no valor de: R${:.2f}'.format((carSpeed - 80) * 7))
else:
    print('Boa viagem!')