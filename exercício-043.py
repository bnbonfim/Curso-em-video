peso = float(input('Qual é o seu peso? (Kg):'))
altura = float(input('Qual é a sua altura?(m):'))
imc = peso / (altura * altura) #peso / (altura ** 2)
if imc <= 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f}, peso ideal!'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f}, está com sobrepeso!'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.2f}, está com obesidade!'.format(imc))
else:
    print('Seu IMC é de {:.2f}, está com obesidade mórbida! Procure um médico.'.format(imc))
