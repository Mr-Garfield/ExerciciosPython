'''
Projeto: Sequência de Fibonacci v.1.0
'''

number = int(input('Quantos números você deseja ver da sequência de Fibonacci? '))

counter = 2
firstTerm = 0
secondTerm = 1
thirdTerm = None

if number != 0:
    if number == 1:
        print('{} -> FIM'.format(firstTerm))
    elif number == 2:
        print('{} -> {} -> FIM'.format(firstTerm, secondTerm))
    else:
        print('{} -> {} -> '.format(firstTerm, secondTerm), end='')

        while counter < number:
            # t3 = t1 + t2
            thirdTerm = firstTerm + secondTerm
            print('{} -> '.format(thirdTerm), end='')
            firstTerm = secondTerm
            secondTerm = thirdTerm
            counter += 1
        print('FIM')

else:
    print('Nenhum número da sequência de Fibonacci foi mostrado!')


