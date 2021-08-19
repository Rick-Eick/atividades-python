# Separando dígitos de um número
N = int(input('Informe um número: '))
u = N // 1 % 10
d = N // 10 % 10
c = N // 100 % 10
m = N // 1000 % 10
print('Analisando o número {}'.format(N))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Unidades de milhar: {}'.format(m))
