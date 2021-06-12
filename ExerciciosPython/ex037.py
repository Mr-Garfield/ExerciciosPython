'''
Projeto: Conversão de bases numéricas
'''
val = int(input('Digite um valor inteiro: '))
print('-'*20)
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('-'*20)
base = int(input('Escolha uma das opções para converter: '))

if base == 1:
    print('{} convertido para BINÁRIO {}'.format(val, bin(val)[2:]))
elif base == 2:
    print('{} convertido para OCTAL {}'.format(val, oct(val)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL {}'.format(val, hex(val)[2:]))
else:
    print('Opção inválida, tente novamente.')
