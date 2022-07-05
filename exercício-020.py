import random
um = str(input('Aluno um:'))
do = str(input('Aluno dois:'))
tr = str(input('Aluno três:'))
qu = str(input('Aluno quatro:'))
l = [um, do, tr, qu]
random.shuffle(l)
print('A ordem dos alunos é: {}'.format(l))

###
from random import shuffle
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
l = [a1, a2, a3, a4]
shuffle(l)
print('A apresentação segue na seguinte ordem {}'.format(l))
