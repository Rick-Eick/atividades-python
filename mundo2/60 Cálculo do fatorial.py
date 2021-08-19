# Cálculo do fatorial
n = int(input('Digite um número para saber o seu Fatorial: '))
m = 1
print('A operação de {}! igual A: ({} x '.format(n, n), end='')
while n >= 1:
    m *= n
    n = (n - 1)
    print('{}'.format(n)[::-1], end='')
    print(' x ' if n > 0 else ')', end='')
print('\nResulta em um Fatorial de {}.'.format(m))
