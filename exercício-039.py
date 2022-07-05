from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu?'))
sexo = str(input('Qual é o seu gênero? (digite Feminino ou Masculino):'))
idade  = atual - ano
if sexo == 'Feminino':
    print('\033[95mPara pessoas do sexo feminino o alistamento não é obrigatório\033[m')
elif idade == 18 and sexo == 'Masculino':
    print('Quem nasceu no ano de {} tem {} em {}'.format(ano, idade, atual))
    print('Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m')
elif idade > 18 and sexo == 'Masculino':
    print('Quem nasceu no ano de {} tem {} em {}'.format(ano, idade, atual))
    saldo = idade - 18
    print('Você deveria ter se alistado há \033[91m{} ano(s)\033[m'.format(saldo))
    print('\033[33mSeu alistamento foi em {}\033[m'.format(atual - saldo))
elif idade < 18 and sexo == 'Masculino':
    print('Quem nasceu no ano de {} tem {} em {}'.format(ano, idade, atual))
    saldo = 18 - idade
    print('Ainda falta {} ano(s) para voce se alistar'.format(saldo))
    print('Seu alistamento será em {}'.format(atual + saldo))
