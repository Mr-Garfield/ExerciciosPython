"""
Projeto: Função para votação
"""

from datetime import date

def Voto(bornYear):
    age = date.today().year - bornYear
    if age < 18:
        return f'Com {age} anos: VOTO NEGADO'
    elif 18 <= age < 65:
        return f'Com {age} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {age} anos: VOTO OPCIONAL'

bornYear = int(input('Em que ano você nasceu? '))
print(Voto(bornYear))
