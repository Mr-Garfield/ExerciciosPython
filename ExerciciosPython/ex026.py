'''
Projeto: Priemeira e última ocorrência de uma strig
'''

sentence = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} nessa frase.'.format(sentence.count('a')))
print('A primeira letra A apareceu na posição {}'.format(sentence.find('a')+1))
print('A última letra A apareceu na posição {}'.format(sentence.rfind('a')+1))

