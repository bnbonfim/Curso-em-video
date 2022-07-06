mediaidade = 0
novo = 0
velho = 0
maioridade = 0
totmulher = 0
for pessoa in range(1, 5):
    nome = str(input('Qual é o nome da {}ª pessoa? '.format(pessoa))).strip().title()
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(pessoa)))
    sexo = str(input('Qual é o sexo da {}ª pessoa[f/m]? '.format(pessoa))).strip()
    mediaidade += idade
    if pessoa == 1 and sexo in 'm':
        maioridade = idade
        velho = nome
    if sexo in 'm' and idade > maioridade:
        maioridade = idade
        velho = nome
    if idade < 20 and sexo in 'f':
        totmulher += 1
print('A média de idade do grupo é {}'.format(mediaidade/4))
print('O mais velho do grupo é {} com {} anos'.format(velho, maioridade))
print('O total de mulheres com menos de 20 anos é de {}'.format(totmulher))
