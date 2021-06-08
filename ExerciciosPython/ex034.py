'''
Projeto: Aumentos múltiplos
'''
s = float(input('Qual o seu salário? R$'))
if s > 1250:
    novo = s * 0.1 + s
else:
    novo = s * 0.15 + s
print('Você ganhava R${:.2f} e vai passar a ganhar R${:.2f}'.format(s, novo))
