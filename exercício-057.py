s = 'F', 'M'
while s != 'F' and s != 'M':#só aceitar M/F
    s = str(input('Digite o sexo utilizando somente M/F: ')).strip().upper()[0]# Ler o sexo da pessoa
    if s != 'F' and s != 'M':
        print('Por favor, digite a informação correta!')
print('Informação armazenada')
