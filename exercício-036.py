v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Em quantos anos pretende pagar a casa?:'))
p = v / (a * 12)
m = s * 30 / 100
print('Para pagar uma casa de R${:.2f} por {} anos a prestação será de R${:.2f}'.format(v, a, p))
if p <= m:
    print('Empréstima pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
