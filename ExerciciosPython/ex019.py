'''
Projeto: Sorteia nome dos alunos
'''
import random

while True:
    a1 = input('Primeiro aluno: ')
    a2 = input('Segundo aluno: ')
    a3 = input('Terceiro aluno: ')
    a4 = input('Quarto aluno: ')
    lista = [a1, a2, a3, a4]
    print('O aluno esolhido foi {}'.format(random.choice(lista)))