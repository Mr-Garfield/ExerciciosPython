'''
Projeto: Conversão de bases numéricas
'''

number = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
option = int(input('Ecolha uma opção: '))
if option == 1:
    print('O número {} em Binário: {}'.format(number, bin(number)[2:]))
elif option == 2:
    print('O número {} em Octal: {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('O número {} em Hexadecimal: {}'.format(number, hex(number)))
else:
    print('Opção inválida, tente novamente!')