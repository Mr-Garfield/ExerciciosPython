'''
Projeto: Soma de ímpares múltiplos de 3
'''

sum = 0

for multiple in range(1, 501, 2):
    if multiple % 3 == 0:
        sum += multiple
print(sum)