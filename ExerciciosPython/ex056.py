'''
Projeto: Analisador Completo
'''
mais_velho = []
lista_nomes = []
lista_idades = []
contadorM = 0
pos_maisVelhor = 0

for c in range(1,5):
    print(f'{c}° Pessoa:')
    n = input('Digite seu nome: ')
    lista_nomes.append(n)
    i = int(input('Digite sua idade: '))
    lista_idades.append(i)
    print('-'*15)
    print('[1] MASCULINO')
    print('[2] FEMININO')
    print('[3] OUTRO')
    print('-' * 15)
    g = int(input('Digite seu gênero: '))
    if g == 2 and i < 20:
        contadorM += 1
    elif g == 1:
        mais_velho.append(i)
        pos_maisVelhor = mais_velho.index(max(lista_idades))
    print('')

print(f'A média de idade do grupo é {sum(lista_idades)/4:.2f}')
print(f'O homem mais velho têm {lista_idades[pos_maisVelhor]} e seu nome é {lista_nomes[pos_maisVelhor]}')
print(f'O número de mulheres com menos de 20 anos é {contadorM}')