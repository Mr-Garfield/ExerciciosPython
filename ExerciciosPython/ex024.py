'''
Projeto: Verificando a primeira palavra é 'SANTO'
'''
c = input('Qual o nome da sua cidada? ')
c = c.upper().split()
s = 'SANTO' in c[0]
print(s)