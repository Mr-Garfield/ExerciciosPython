"""
Projeto: Média de aluno com dicionário
"""

student = dict()

student['name'] = input('Nome: ')
student['media'] = float(input(f'Média de {student["name"]}: '))

if student['media'] >= 7:
    student['situation'] = "APROVADO"
elif 5 <= student['media'] < 7:
    student['situation'] = "RECUPERACAO"
else:
    student['situation'] = "REPROVADO"


print(f'A situação é igual a {student["situation"]}')

