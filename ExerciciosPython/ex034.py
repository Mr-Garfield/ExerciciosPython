'''
Projeto: Cálculo de aumento para diferentes salários
'''

salary = float(input('Digite seu salário: R$ '))

porcentage = '15%'
if salary <= 1250:
    salaryIncrease = salary + (salary * 0.15)
else:
    salaryIncrease = salary + (salary * 0.10)
    porcentage = '10%'
print('Parabéns, com o auamento de {} você passa a receber: R${:.2f}'.format(porcentage, salaryIncrease))