# Analisador completo
Cont = 0
Maior = 0
Media = 0
Homem = ''
for C in range(1, 5):
    print('-----{}º PESSOA-----'.format(C))
    Nome = str(input('NOME: '))
    Idade = int(input('IDADE: '))
    Sexo = str(input('SEXO [M/F]:'))
    Media += Idade
    if Sexo == 'M':
        if Maior < Idade:
            Maior = Idade
            Homem = Nome
    if Sexo == 'F' and Idade < 20:
        Cont += 1
Media = Media / 4
print('A média das idades é {}'.format(Media))
print('O homem mais velho tem {} anos e se chama {}'.format(Maior, Homem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(Cont))
