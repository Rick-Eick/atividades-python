# Criando um menu de opções
from time import sleep
v = 0
op = '4'
n1 = 0
n2 = 0
while v != 5:
    while op == '4':
        n1 = int(input('Digite Um Valor: '))
        n2 = int(input('Digite Outro Valor: '))
        op = 0
    print('=-=' * 20)
    op = str(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair Do Programa '''))
    if op == '1':
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif op == '2':
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif op == '3':
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 == n2:
            print('Os números são iguais')
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif op == '4':
        print('Escolha os novos números')
    elif op == '5':
        v = 5
        print('Finalizando...')
        sleep(3)
        print('Fim do programa.')
    else:
        print('Valor inválido, tente novamente.')
    sleep(2)
