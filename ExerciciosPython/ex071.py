"""
Projeto: Simulado caixa
"""

print('=+='*15)
print('SIMULADOR CAIXA ELETRÔNICo'.center(45))
print('=+='*15)

money = int(input('Digite o valor que deseja sacar: R$'))
print('Você vai receber: ')


bankNote = 50
totalBankNotes = 0
amount = money

while True:
    if amount >= bankNote:
        amount -= bankNote
        totalBankNotes += 1

    else:
        if totalBankNotes != 0:
            print(f'{totalBankNotes} cédulas de R${bankNote}')
        if bankNote == 50:
            bankNote = 20

        elif bankNote == 20:
            bankNote = 10

        elif bankNote == 10:
            bankNote = 1

        totalBankNotes = 0

        if amount == 0:
            break




