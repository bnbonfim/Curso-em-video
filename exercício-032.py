a = int(input('Digite um ano:'))
d = a % 4 == 0
e = a % 100 != 0
f = a % 400 == 0
print('É bissexto'if a == a and e or f else'Não é bissexto')

###
from datetime import date
ano = int(input('Digite o ano que quer analisar ou digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('O ano {} é bisssexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
