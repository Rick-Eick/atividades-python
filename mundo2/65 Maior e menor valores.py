# Maior e menor valores
Maior = 0
Menor = 0
soma = cont = r = 0
while r != 1:
    n = float(input('Digite um número: '))
    if cont == 0:
        Maior = Menor = n
    else:
        if n > Maior:
            Maior = n
        elif n < Menor:
            Menor = n
    soma += n
    cont += 1
    c = input('Quer continuar? [S/N]').strip().upper()[0]
    while c != 'S' and c != 'N':
        c = input('Opão inválida, favor tentar novamente: [S/N]').strip().upper()[0]
    if c == 'S':
        r = 0
    else:
        r = 1
print('''Você digitou {} números com média {:.1f}
O maior foi {} e o menor foi {}'''.format(cont, soma/cont, Maior, Menor))
