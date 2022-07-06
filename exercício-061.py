t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
pa = 0
print(t1, ',', end='')
while pa < 9:
    pa += 1
    pt = pa * r + t1
    print('{}'.format(pt), end=', ')
print('Acabou!')
