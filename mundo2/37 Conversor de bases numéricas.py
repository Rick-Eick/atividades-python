# Conversor de bases numéricas
n1 = int(input('Digite um número inteiro: '))
A = bin(n1)
B = oct(n1)
C = hex(n1)
print('='*35)
print('''ESCOLHA A FORMA DE CONVERSÃO
[1] Binário.
[2] Octal.
[3] Hexadecimal.''')
print('='*35)
p1 = int(input('Opção: '))
if p1 == 1:
    print('O número em forma binária é {}!'.format(A))
elif p1 == 2:
    print('O número em octal é {}!'.format(B))
elif p1 == 3:
    print('O número em forma hexadecimal é {}!'.format(C))
else:
    print('='*35, 'DANGER ALERT', '='*35)
    print('  '*34, 'Escolha invalída!')
    print('=' * 35, 'DANGER ALERT', '=' * 35)
