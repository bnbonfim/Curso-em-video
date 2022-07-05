a = float(input('Primeiro número:'))
b = float(input('Segundo número:'))
c = float(input('Terceiro número:'))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
maior = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {:.0f}'.format(menor))
print('O maior valor digitado foi: {:.0f}'.format(maior))
