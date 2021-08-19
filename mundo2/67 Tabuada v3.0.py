# Tabuada v3.0
N = int(input('Digite um número para ver sua tabuada: '))
while N != 0:
    print('='*14)
    for C in range(0, 11):
        print('{} X {} = {}'.format(N, C, N * C))
    print('='*14)
    N = int(input('Digite um número para ver sua tabuada: '))
print('FIM DO PROGRAMA')
