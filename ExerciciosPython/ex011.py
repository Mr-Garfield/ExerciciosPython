'''
Projeto: Calculando tinta para parede.
'''
l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
area = l * h
tinta = area / 2
print('Sua parede tem {}x{} e sua área é de {:.2f}m².'.format(l, h, area))
print('Para pintar a parede, você precisará de {:.2f}l de tinta.'.format(tinta))