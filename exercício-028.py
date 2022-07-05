p = float(input('Estou pensando em um número entre 0 e 5, dê seu palpite:'))
n = '4'
print('VOCÊ ACERTOU'if p == 4 else'TENTE NOVAMENTE!')
###

from random import randint
from time import sleep
comp = randint(0, 5) #faz o computador "pensar"
print('-*-' * 20)
print('Estou pensando em um numero entre 0 e 5, tente adivinhar:')
print('-*-' * 20)
print('PENSANDO...')
sleep(2)
joga = int(input('Qual o seu palpite?:')) #Jogador advinha
print('ATENÇÃO!')
sleep(2)
if joga == comp:
    print('VOCÊ ACERTOU, EU PENSEI EM {}'.format(joga))
else:
    print('EU GANHEI, PENSEI EM {} E NÃO {}'.format(comp, joga))
