dis = float(input('Qual a distãncia da sua viagem? Km:'))
print('O valor foi de R${:.2f}'.format(dis * 0.45)if dis > 200 else'O valor foi de R${:.2f}'.format(dis * 0.50))
