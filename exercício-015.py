t = float(input('Digite por quantos dias o carro foi alugado:'))
c = float(input('Digite quantos Km foram percorridos com o carro: Km'))
d = (t * 60) + (c * 0.15)
print('O valor a pagar com a utilização do carro é de {:.2f}'.format(d))
