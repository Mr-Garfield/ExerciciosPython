'''
Projeto: Sortear um aluno
'''

import random

studentA = input('Primeiro aluno: ')
studentB = input('Segundo aluno: ')
studentC = input('Terceiro aluno: ')
studentD = input('Quarto aluno: ')
students = [studentA, studentB, studentC, studentD]
print('O aluno que deve apresentar primeiro é o(a): {}'.format(random.choice(students)))