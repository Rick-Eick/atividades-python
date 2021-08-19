# Comparando números
from time import sleep
N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))
print('Calculando a resposta...')
sleep(1.5)
if N1 > N2:
    print('O maior número é {}'.format(N1))
    print('E menor é {}'.format(N2))
elif N2 > N1:
    print('O maior é {} '.format(N2))
    print('O menor número é {}'.format(N1))
else:
    print('Os números são iguais.')
