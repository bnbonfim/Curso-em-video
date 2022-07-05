r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta:'))
r3 = float(input('Terceira reta:'))
print('Formam um triângulo!'if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 else'Não formam um triângulo!')
