import random
print('-'*10, 'SORTEIO', '-'*10)
a1 = str(input('Aluno um:'))
a2 = str(input('Aluno dois:'))
a3 = str(input('Aluno três:'))
a4 = str(input('Aluno quatro:'))
s = random.choice((a1, a2, a3, a4))
print('O aluno escolhido para apagar o quadro hoje foi:{}'.format(s))

####
from random import choice
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o Aluno escolhido para apagar o quadro foi:{}'.format(escolhido))
