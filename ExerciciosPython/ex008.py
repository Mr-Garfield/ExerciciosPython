'''
Projeto: Conversor de medidas
'''
m = float(input('Uma distância em metros: '))
cm = m * 100
mm = m * 1000
print('A a medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(m, cm, mm))
print(' ')
#print('A medida de {}m corresponde a '. format(m))
print('{}km'.format(m/1000))
print('{}hm'.format(m/100))
print('{}dam'.format(m/10))
print('{:.0f}dm'.format(m*10))
print('{:.0f}cm'.format(m*100))
print('{:.0f}mm'.format(m*1000))