nota1 = float(input('1ª nota:'))
nota2 = float(input('2ª nota:'))
media = (nota1 + nota2) / 2
print('A média entre as notas {} e {} é de {}, portanto o aluno está:'.format(nota1, nota2, media))
if media <= 5.0:
    print('REPROVADO!')
elif media >= 7.0:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO!')
