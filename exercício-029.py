v = float(input('A que velocidade o carro andava? Km:'))
vp = '80'
m = (v - 80) * 7
print('Você foi multado, ultrapassou o limite de 80Km/h')
print('Sua multa ficará no valor de R${:.2f}'.format(m) if v > 80 else'Sua velocidade está de acordo!')

###

velocidade = float(input('Qual a velocidade atual do carro?:'))
if velocidade > 80:
    print('MULTADO! Você passou o limete de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Voce receubeu uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
