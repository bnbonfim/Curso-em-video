termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for p in range(termo, 10 * razao + termo, razao):
    print('{}'.format(p), end=', ')
print('ACABOU!')
