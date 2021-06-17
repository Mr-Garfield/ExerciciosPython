'''
Projeto: Maior e Menor Peso
'''
massa_lista = []

for p in range(1,6):
    massa = float(input('Digite seu peso: '))
    massa_lista.append(massa)

print('O menor peso digitado foi {:.2f}kg'.format(min(massa_lista)))
print('E o maior ditado foi {:.2f}kg'.format(max(massa_lista)))