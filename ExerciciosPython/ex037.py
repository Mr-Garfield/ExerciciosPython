'''
Projeto: Conversão de bases numéricas
'''
val = int(input('Digite um valor que deseja converter: '))
print('-'*20)
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('')
print('Escolha uma das opções ACIMA!!!')
print('-'*20)
base = int(input('Escolha uma das opções para converter: '))

if base == 1:
    print('{} convertido para BINÁRIO {}'.format(val, bin(val)))
elif base == 2:
    print('{} convertido para OCTAL {}'.format(val, oct(val)))
elif base == 3:
    print('{} convertido para HEXADECIMAL {}'.format(val, hex(val)))
else:
    print('Opção inválida, tente novamente.')
