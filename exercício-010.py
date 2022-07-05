r = float(input('Quanto você possui em sua carteira?: R$'))
d = r / 5.12
e = r / 5.61
print('Com R${:.2f}, você pode comprar:\nUS${:.2f} em Dólar!\n€{:.2f} em Euro'.format(r, d, e))
