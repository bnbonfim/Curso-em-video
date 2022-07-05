import math
a = float(input('Digite um Ângulo:'))
c = math.cos(a)
s = math.sin(a)
t = math.tan(a)
print('Aqui estão os valores para {}\nSeno:{}\nCosseno:{}\nTângente:{}'.format(a, s, c, t))

###

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o seno de{:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem cosssemo de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a tângente de {:.2f}'.format(angulo, tangente))
