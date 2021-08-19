# GAME: par ou ímpar
from random import randint
v = 0
while True:
    print('='*25)
    print('VAMOS JOGAR PAR OU IMPAR?')
    print('='*25)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in ('P', 'I'):
        tipo = str(input('Par ou impar [P/I]: ')).upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    else:
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes')
