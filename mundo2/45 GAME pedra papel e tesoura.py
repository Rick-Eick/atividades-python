# GAME: pedra, papel e tesoura
from random import choice
Opcoes = ['pedra', 'papel', 'tesoura']
Adv = choice(Opcoes)
print('Digite qual você quer jogar!')
jogador = str(input('PEDRA, PAPEL ou TESOURA? ')).lower().strip()
if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
    print('Você jogou {} e eu joguei {}.'.format(jogador.upper(), Adv.upper()))
    if Adv == jogador:
        print('Nós empatamos!')
    elif Adv == 'pedra' and jogador == 'papel':
        print('Você ganhou!')
    elif Adv == 'pedra' and jogador == 'tesoura':
        print('Eu ganhei!')
    elif Adv == 'papel' and jogador == 'pedra':
        print('Eu ganhei!')
    elif Adv == 'papel' and jogador == 'tesoura':
        print('Você ganhou!')
    elif Adv == 'tesoura' and jogador == 'pedra':
        print('Você ganhou!')
    elif Adv == 'tesoura' and jogador == 'papel':
        print('Eu ganhei!')
    else:
        print('Erro!')
