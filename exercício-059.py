import time
escolha = ''
menu = 0
print('=-' * 14)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('=-' * 14)
while escolha != 5:
    menu = (' [1]Para Somar\n [2]Para Multiplicar\n [3]Para o Maior\n [4]para Novos números\n [5]Para sair do programa')
    print('=-' * 14)
    print(menu)
    print('=-' * 14)
    escolha = int(input('Qual é a sua escolha? '))
    if escolha == 1:
        soma = n1 + n2
        print('=-' * 14)
        print('A soma dos números é: {}'.format(soma))
    elif escolha == 2:
        multi = n1 * n2
        print('=-' * 14)
        print('A multiplicação dos números\né igual a: {}'.format(multi))
    elif escolha == 3:
        if n1 > n2:
            print('=-' * 14)
            print('O maior é {}'.format(n1))
        else:
            print('=-' * 14)
            print('O maior é {}'.format(n2))
    elif escolha == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Aguarde...')
    else:
        print('Opção invalida! Tente novamente.')
time.sleep(2)
print('Programa finalizado!')
print('-' * 20)
