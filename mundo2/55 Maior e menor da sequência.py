# Maior e menor da sequência
Maior = 0
Menor = 0
for C in range(1, 6):
    Peso = float(input('Peso da {}º pessoa: '.format(C)))
    if C == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
        if Peso < Menor:
            Menor = Peso
print('O maior peso lido foi {}'.format(Maior))
print('O menor peso lido foi {}'.format(Menor))
