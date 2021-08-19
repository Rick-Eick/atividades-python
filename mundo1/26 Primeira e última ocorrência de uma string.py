# Primeira e última ocorrência de uma string
Frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(Frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(Frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(Frase.rfind('A')+1))
