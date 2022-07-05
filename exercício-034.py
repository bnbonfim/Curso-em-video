s = float(input('Qual o atual sálario?:'))
ss = s * 10 / 100
si = s * 15 / 100
print('O novo sálario é de R${:.2f}'.format(s + ss)if s >= 1250 else'o novo salário é de {:.2f}'.format(s + si))
###
salario = float(input('Salário atual:'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem passava a ganhar R${:.2f}, agora ganha R${:.2f}'.format(salario, novo))
