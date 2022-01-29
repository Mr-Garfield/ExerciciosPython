"""
Projeto: Validando expressões matemáticas
"""

expression = input('Digite uma expressão matemática: ')

parentheses = list()

for c in expression:
    if c == '(':
        parentheses.append(c)
    elif c == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            break

if len(parentheses) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')

# Solução utilizando o count
""" 
if expression.count('(') == expression.count(')'):
    print('A expressão está completa.')
else:
    print('A expressão é inválida.')
"""
