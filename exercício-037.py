print('\033[45m=\033[m' * 28)
print('\033[35mConversor de bases númericas\033[m')
print('\033[45m=\033[m' * 28)
num = int(input('\033[1;95mDigite um número inteiro\033[m:'))
bc = int(input('(1) para binário\n(2) para octal\n(3) para hexadecimal\nSua opção:'))
print('O número {} na opção escolhida é :'.format(num))
if bc == 1:
    print(bin(num)[2:])
elif bc == 2:
    print(oct(num)[2:])
elif bc == 3:
    print(hex(num)[2:])
else:
    print('OPÇÃO INVÁLIDA!')
