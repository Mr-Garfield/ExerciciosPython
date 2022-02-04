"""
Projeto: Mensagem adaptável
"""

def Escreva(msg):
    mensageSize = len(msg) + 4
    print('~'* mensageSize)
    print(msg.center(mensageSize))
    print('~'* mensageSize)

Escreva('Vitinho Tech - Youtube')