n = int(input('Digite um numero: '))
mult = 0
for p in range(1, n + 1):
    if n % p == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[32m', end='')
    print('{}'.format(p), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(n, mult))
if mult == 2:
    print('É um número primo!')
else:
    print('Não é primo!')
