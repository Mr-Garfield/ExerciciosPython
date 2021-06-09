'''
Projeto: Calculando financeamento de casa
'''
valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos você pretende pagar a casa? '))
parcelas = valorCasa / (anos * 12)

if parcelas <= (salario * 0.3):
    print('Seu empréstimo foi APROVADO!!!')
    print('Voce pagará {:.0f} parcelas de {:.2f}.'.format(anos*12, parcelas))
else:
    print('Lamentamos, seu empréstimo NÃO foi aprovado!')