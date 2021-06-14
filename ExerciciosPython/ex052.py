'''
Projeto: Números primos
'''
n = float(input('Digite um número para saber se ele é primo ou não: '))
primo = False
for c in range(1, 9):

    if n != c and n % c == 0:
        #Não é primo
        primo = False
    else:
        primo = True

if primo == True:
    print('{} é um número primo'.format(n))
else:
    print('{} NÃO é um número primo.'.format(n))