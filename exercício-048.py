s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} multiplos e ímpares é {}'.format(cont, s))
