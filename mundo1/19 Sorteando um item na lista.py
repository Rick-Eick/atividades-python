# Sorteando um item na lista
import random
A1 = input('Nome do aluno: ')
A2 = input('Nome do aluno: ')
A3 = input('Nome do aluno: ')
A4 = input('Nome do aluno: ')
Lista = [A1, A2, A3, A4]
print('o escolhido foi {}'.format(random.choice(Lista)))
