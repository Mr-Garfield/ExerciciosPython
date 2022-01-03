'''
Projeto: Pintando parede (cada litro pinta 2m²)
'''

l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

litros = (l * h) / 2

print('Sua parede tem {:.2f}m² e será necessário {:.2f}l de tinta para pintar.'.format(l * h, litros))