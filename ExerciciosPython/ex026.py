'''
Projeto: - Conta quantas vezes aparece uma letra.
         - Em que posição ela aparece a primeira vez.
         - Em que posição ela aparece a última vez.
'''
phase = input('Digite uma frase: ').lower().strip()

print('A letra A aparece {} vezes na frase.'.format(phase.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(phase.find('a') + 1))
print('A última letra A apareceu na posição {}'.format(phase.rfind('a') + 1))