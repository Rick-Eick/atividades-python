# Alistamento militar
from datetime import date
Atual = date.today().year
Nascimento = int(input('Qual o seu ano de nascimento? '))
Idade = Atual - Nascimento
if Idade == 18:
    print('Corra para se alistar já! ')
elif Idade < 18:
    print(
        f'Falta {18 - Idade} anos para você se alistar, compareça para o alistamento no ano de {Atual + (18 - Idade)}.')
else:
    print('Você ja passou da idade de se alistar, deveria ter se alistado em {}'.format(Atual - (Idade - 18)))
