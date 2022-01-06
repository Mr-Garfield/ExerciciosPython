'''
Projeto: Sorteando ordem de nomes
'''

import random

nameA = input('Primeiro nome: ')
nameB = input('Segundo nome: ')
nameC = input('Terceiro nome: ')
nameD = input('Quarto nome: ')
list = [nameA, nameB, nameC, nameD]
random.shuffle(list)
print('A ordem de nomes sorteados é: \n{}'.format(list))