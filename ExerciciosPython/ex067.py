"""
Projeto: Tabuada v.3.0
"""

while True:
    number = int(input('Digite um número para ver sua tabuada: '))
    print('=+='*5)
    if number < 0:
        break
    else:
        for tableNumber in range(1, 11):
            print(f'{number} x {tableNumber:2} = {number * tableNumber}')
    print('=+=' * 5)
print('FIM')
