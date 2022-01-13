'''
Projeto: Detector de palíndromo
'''

phrase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

palindrome = phrase[::-1]

if phrase == palindrome:
    print('A frase {} é um PALÍNDROMO'.format(palindrome))

else:
    print('A frase {} NÃO é um PALÍNDROMO'.format(palindrome))
