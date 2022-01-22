"""
Projeto: Estatística de produtos
"""

print('=+='*15)
print('LOJA MULTICOISAS'.center(45))
print('=+='*15)

purchaseValue = 0
priceProduct = 0
counter = 0
cheapestProduct = 0
nameCheapestProduct = None

while True:

    productName = input('Nome do produto: ')
    price = float(input('Valor: R$ '))

    purchaseValue += price
    counter += 1

    if counter == 1:
        cheapestProduct = price
        nameCheapestProduct = productName

    if price > 1000:
        priceProduct += 1

    if price < cheapestProduct:
        cheapestProduct = price

    option = input('Quer continuar? [S/N] ').upper().strip()[0]

    if option == 'N':
        break

print('-'*15, ' FIM ', '-'*15)
print(f'O preço da compra foi R${purchaseValue:.2f}')
print(f'{priceProduct} produto(s) custam mais de R$ 1000.00')
print(f'O produto mais barato foi o(a) {nameCheapestProduct} custando R${cheapestProduct:.2f}')
