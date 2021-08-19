# Classificando atletas
from datetime import date
Atual = date.today().year
Nascimento = int(input('Digite seu ano de nascimento: '))
Idade = Atual - Nascimento
print('O atleta tem {} anos'.format(Idade))
if Idade in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    print('Classificação MIRIM')
elif Idade in (10, 11, 12, 13, 14):
    print('Classificação INFANTIL')
elif Idade in (15, 16, 17, 18, 19):
    print('Classificação JÚNIOR')
elif Idade in (20, 21, 22, 23, 24, 25):
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
