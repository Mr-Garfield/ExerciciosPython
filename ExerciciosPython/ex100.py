"""
Projeto:
"""

from random import randint
from time import sleep

numbers = list()

def Sortear():
    print('Sorteando 5 valores da lista: ')
    for n in range(0, 5):
        numberDrawn = randint(1, 10)
        print(numberDrawn, end=' ')
        numbers.append(numberDrawn)
        sleep(0.5)
    print('PRONTO!')

def Somar():
    adder = 0
    for x in numbers:
        if x % 2 == 0:
            adder += x

    print(f'Somando os valores pares de {numbers}, teremos {adder}')

Sortear()
Somar()