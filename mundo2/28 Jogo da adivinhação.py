# Jogo da advinhação
from random import randint
from time import sleep
A = randint(0, 5)
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADVINHA')
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
B = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if A == B:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(A, B))
