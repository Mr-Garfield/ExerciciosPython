"""
Projeto: Funcao Fatorial
"""
def Fatorial(n, show=False):
    '''
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    '''

    fatorial = 1
    for n in range(n, 0, -1):
        fatorial *= n
        if show == True:
            if n != 1:
                print(n, end=' x ')
            else:
                print(n, end=' = ')
    return fatorial

print(Fatorial(5, True))
help(Fatorial)