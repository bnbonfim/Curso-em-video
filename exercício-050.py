s = 0
cont = 0
for c in range(1, 7):
    n = int(input(('digite o valor nº{}: '.format(c))))
    if n % 2 == 0:
        s += n
        cont += 1
print('você informou {} números pares e a soma entre eles é: {}'.format(cont, s))
