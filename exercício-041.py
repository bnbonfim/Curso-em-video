from datetime import date
print('='*30)
print('\033[7;49;32mQual a categoria do seu atleta\033[m')
print('='*30)
ano = int(input('\033[93mQual o ano de nascimento?:'))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos\nportanto é um atleta:'.format(ano, idade))
if idade <= 9:
    print('\033[0;47mAtleta MIRIM\033[m')
elif idade <= 14:
    print('\033[0;43mAtleta INFANTIL\033[m')
elif idade <= 19:
    print('\033[0;41mAtleta JUNIOR\033[m')
elif idade <= 25:
    print('\033[0;45mAtleta SÊNIOR\033[m')
else:
    print('\033[0;40;37mMESTRE\033[m')
