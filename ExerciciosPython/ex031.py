'''
Projeto: Custo da viagem
'''
distance = float(input('Qual a foi a distância percorrida? '))

if distance <= 200:
    val = distance * 0.50
else:
    val = distance * 0.45
print('E o preço preço da sua pasagem será R${:.2f}'.format(val))
print('Você está prestes a começar uma viagem de {}Km.'.format(distance))

