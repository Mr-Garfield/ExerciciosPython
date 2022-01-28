"""
Projeto: Mostrando as vogais em uma tupla
"""

words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programando', 'futuro')

for w in words: # Analisa cada palavra da tupla
    print(f'\nNa palavara {w.upper()} temos: ', end=' ')

    for letters in w: # Analisa cada letra da palavra

        if letters in 'aeiou':
            print(letters, end=' ')

