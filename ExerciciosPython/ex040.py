'''
Projeto: Cálculo de Média
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {:.1f}. REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {:.1f}. RECUPERAÇÃO!'.format(media))
else:
    print('Sua média foi {:.1f}. Parabéns, APROVADO!'.format(media))