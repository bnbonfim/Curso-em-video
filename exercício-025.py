nome = str(input('Me diga seu nome:')).title().split()
sn = 'Silva' in nome[0:]
print(sn)
##
nome = str(input('Digite seu nome?:'))
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))
