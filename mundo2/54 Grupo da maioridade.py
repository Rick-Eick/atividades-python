# Grupo da maioridade
ContM = 0
ContN = 0
for C in range(1, 8):
    A = int(input('Digite a data de nascimento da {}º pessoa: '.format(C)))
    if 2019 - A >= 18:
        ContM += 1
    else:
        ContN += 1
print('Nesse grupo de pessoas há:')
print('{} pessoas maiores de idade e'.format(ContM))
print('{} pessoas menores de idade'.format(ContN))
