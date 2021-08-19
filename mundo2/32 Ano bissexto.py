# Ano Bissexto
from datetime import date
Ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(Ano))
else:
    print('O ano {} não é BISSEXTO'.format(Ano))
