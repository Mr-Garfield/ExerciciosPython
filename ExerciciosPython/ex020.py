'''
Projeto: Sorteia ordem de nomes
'''
import random

n1 = input('Primeiro nome: ')
n2 = input('Quarto nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de que vai apresentar é: ')
print(lista)