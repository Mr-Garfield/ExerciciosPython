'''
Projeto: Aluguel de carros
'''

quilometros = float(input('Quilômetros percorridos: '))
dias = int(input('Quantidade de dias em posse do automóvel: '))
preco = (quilometros * 0.15) + (dias * 60)
print('O valor a pagar é: R${:.2f}'.format(preco))
