num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
if num1 == num2:
    print('Não existe valor maior, os dois são iguais!')
elif num1 > num2:
    print('\033[91mPRIMEIRO é o maior numero!\033[m')
else:
    print('\033[91mSEGUNDO é o maior número!\033[m')
