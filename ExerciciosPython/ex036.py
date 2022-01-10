'''
Projeto: Aprovando empréstimo
'''

houseValue = float(input('Digite o valor da casa: R$'))
salary = float(input('Digite o seu salário: R$'))
years = int(input('Digite em quantos anos deseja pagar: '))

installments = houseValue / (years * 12)
salaryPorcentage = salary * (30 / 100)

if installments >= salaryPorcentage :
    print('Lamentamos em dizer que seu empréstimo foi RECUSADO!')
else:
    print('Parabéns!!! Seu empréstimo foi ACEITO.')
    print('Você irá pagar parcelas de R${:.2f} ao logo de {} anos!'.format(installments, years))