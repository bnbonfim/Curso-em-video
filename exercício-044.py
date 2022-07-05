import emoji
print('Lojas Bn {}'.format(emoji.emojize(':face_with_raised_eyebrow:')))
valor = float(input('Qual é o preço do produto?R$:'))
print('"1" para à vista/cheque\n"2" para à vista no cartão\n"3" para até 2x no cartão\n"4" para 3x ou mais no cartão')
pgmt = float(input('Qual a condição de pagamento?:'))
if pgmt == 1:
    d10 = valor * 10 / 100
    print('O preço atual será de R${:.2f}'.format(valor - d10))
elif pgmt == 2:
    d5 = valor * 5 / 100
    print('O preço atual será de R${:.2f}'.format(valor - d5))
elif pgmt == 3:
    print('O preço atual é de R${:.2f}'.format(valor))
elif pgmt == 4:
    d20 = valor * 20 / 100
    p = float(input('Em quantas vezes quer pagar?'))
    parcelas = valor / p
    print('O produto dividido em {:.0f} parcelas pagas no valor de'
          'R${:.2f} com JUROS'.format(p, parcelas))
    print('O preço será de R${:.2f}'.format(valor + d20))
else:
    print('O Valor não corresponde ao pedido! Tente novamente')
