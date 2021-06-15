'''
Projeto: Números primos
'''
'''
boa, OK, acho que sim
'''
from time import sleep


def processando():
    print('PROCESSANDO', end='') #Vou colocar o enunciado na tela
    for time in range(3):
        sleep(0.5)
        print('.', end='')


contador = 0

while True:
    n = int(input('Digite um número para saber se ele É ou NÃO primo: '))
    if n == 0:
        break
    else:
        for i in range(2, n):
            if n % i == 0:
                contador += 1
        if contador == 0:
            print('{} É um número primo'.format(n))
        else:
            print('{} Não é um número primo'.format(n))
        print("Digite '0' para finalizar o programa")
print()
processando()
print()
sleep(2)
print('Foi um prazer ter você conosco, continue estudando :)!')



