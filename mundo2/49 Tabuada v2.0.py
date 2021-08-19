# Tabuada v2.0
N = int(input('Digite um número para ver sua tabuada: '))
print('='*14)
for C in range(0, 11):
    print('{} X {} = {}'.format(N, C, N * C))
print('='*14)
