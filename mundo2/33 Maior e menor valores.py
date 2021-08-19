# Maior e menor valores
N1 = int(input('Digite o primeiro valor: '))
N2 = int(input('Digite o segundo valor: '))
N3 = int(input('Digite o terceiro valor: '))
Menor = N1
if N2 < N1 and N2 < N3:
    Menor = N2
if N3 < N2 and N3 < N1:
    Menor = N3
print('O menor valor digitado foi {}'.format(Menor))
Maior = N1
if N2 > N1 and N2 > N3:
    Maior = N2
if N3 > N2 and N3 > N1:
    Maior = N3
print('O maior valor digitado foi {}'.format(Maior))
