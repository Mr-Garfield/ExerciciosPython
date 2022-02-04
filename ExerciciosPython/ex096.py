"""
Projeto: Função para cálculo de área
"""

def Area(l, c):
    print(f'A área de um terreno {l} x {c} é de {l*c:.1f}m²')

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

Area(l, c)
