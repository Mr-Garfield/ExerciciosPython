"""
Projetos: Times de futebol
"""

brazilianTeams = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
                  'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
                  'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia',
                  'Sport', 'Chapecoense')


print('=+='*7)
print('Lista do Brasileirão: ', brazilianTeams)
print('=+='*7)
print('Os 5 primeiros são: ', brazilianTeams[0:4])
print('=+='*7)
print('Os 4 últimos são: ', brazilianTeams[-4:])
print('=+='*7)
print('Os times em ordem alfabética: ', sorted(brazilianTeams)) # Mostra os nomes em ordem alfabética
print('=+='*7)
print('O Chapecoense está na posição:', brazilianTeams.index('Chapecoense') + 1)
