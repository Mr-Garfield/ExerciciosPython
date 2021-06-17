'''
Projeto: Verificador de Palíndromo
'''
p = input('Digite uma frase para verificar se é um palíndromo: ').replace(' ', '')

if p == p[::-1]:#Lê de traz para frente
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
