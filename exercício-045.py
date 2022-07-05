import emoji
import random
from time import sleep
pedra = emoji.emojize(':raised_fist:')
papel = emoji.emojize(':raised_hand:')
tesoura = emoji.emojize(':victory_hand:')
print('jokenpô {} {} {}'.format(pedra, papel, tesoura))
lista = ['pedra', 'papel', 'tesoura']
print('pedra, papel ou tesoura')
computador = random.choice(lista)
jogador = str(input('Sua escolha:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-'*10)
print(' ' * 5, 'Você escolheu {}\n     e eu escolhi {}' .format(jogador, computador))
print(' ' * 5)
if computador ==                    'pedra':
    if jogador == 'pedra':
        print('EMPATE!!')
    elif jogador == 'papel':
        print('VOCÊ GANHOU!')
    elif jogador == 'tesoura':
        print('EU GANHEI!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 'papel':
    if jogador == 'pedra':
        print('EU GANHEI!!')
    elif jogador == 'papel':
        print('EMPATE!')
    elif jogador == 'tesoura':
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 'tesoura':
    if jogador == 'pedra':
        print('VOCÊ GANHOU!')
    elif jogador == 'papel':
        print('EU GANHEI!')
    elif jogador == 'tesoura':
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
print('-=-'*10)
