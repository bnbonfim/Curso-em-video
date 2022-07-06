f = input('Digite uma frase: ').split(' ')
aux = ''
for p in range(0, len(f)):
    aux += f[p]
if aux.lower() == aux.lower()[::-1]:
    print('Palíndromo')
else:
    print('Não é palíndromo')
