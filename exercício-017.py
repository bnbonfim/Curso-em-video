from math import hypot
print('-'*10, 'Com a fórmula', '-'*10)
co = float(input('Valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente:'))
h = hypot(co, ca)
print('A hipotenusa deste triangulo retãngulo é {:.2f}'.format(h))
