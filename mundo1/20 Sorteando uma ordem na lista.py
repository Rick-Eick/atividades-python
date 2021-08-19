# Sorteando uma ordem na lista
from random import shuffle
A1 = str(input('Nome do aluno: '))
A2 = str(input('Nome do aluno: '))
A3 = str(input('Nome do aluno: '))
A4 = str(input('Nome do aluno: '))
Lista = [A1, A2, A3, A4]
shuffle(Lista)
print('A ordem de apresentação será:')
print(Lista)
