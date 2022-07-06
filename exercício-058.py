from random import randint#importando função para gerar números aleatórios
joga = 0
palpites = 0
comp = randint(0, 10)#gerador de números aleatórios
print('Penso em um número entre 0 e 10...')
while joga != comp:#Enquanto o palpite do jogador for diferente do palpite do computador
    joga = int(input('Qual é o seu palpite?: '))#irá se repetir
    if joga != comp:
        print('Tente novamente:')#irá se repetir somente quando o jogador não acertar!
    if comp > joga:
        print('mais...')
    if comp < joga:
        print('menos...')
    palpites += 1#número de palpites
print('Você acertou com {} palpites!'.format(palpites))
