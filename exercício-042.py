a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('terceiro seguimento:'))
if a < b + c and b < a + c and c < a + b:
    print('Podem formar um triângulo, cuja classificação é:')
    if a == b == c:
        print('Equilátero')
    elif a == b != c or b == c != a or c == a != b:
        print('Isóceles')
    elif a != b != c:
        print('Escaleno')
else:
    print('Não formam um triangulo')
