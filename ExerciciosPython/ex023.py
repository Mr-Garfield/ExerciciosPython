'''
Projetos: Separando dígitos de um número
'''

number = int(input('Informe um número: '))
#Divide o número e pega a parte inteira, depois pega o módulo de 10
print(f'Analizando o número {number}')
print(f'Unidade: {(number // 1) % 10}')
print(f'Dezena: {(number // 10) % 10}')
print(f'Centena: {(number // 100) % 10}')
print(f'Milhar: {(number // 1000) % 10}')
