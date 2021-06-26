'''
Projeto: Calculadora
'''

while True: #Laço de repetição infinito
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))
    print('-'*15)# Lista de opções para o usuário
    print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
    print('-' * 15)
    operador = int(input('Escolha uma opção: ')) # Verifica qual sera a opração escolhida
    if operador == 1:
        print(v1 + v2)
    if operador == 2:
        print(v1 * v2)
    if operador == 3:
        print(max((v1, v2)))
    if operador == 4:
        pass
    if operador == 5: # Caso a opção seja [5] sairá do programa
        print('')
        print('Fechando programa...')
        break