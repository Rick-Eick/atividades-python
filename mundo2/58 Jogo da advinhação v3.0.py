# jogo da advinhação v3.0
from random import randint
from time import sleep
print('''============================================================
♦   Vamos Jogar um jogo? Vou pensar num número de 0 a 5   ♦
============================================================\n''')
sleep(3)
print('''♦ Você tem 5 tentativas!
♦ A cada erro você perde um ponto.
♦ Se você chegar a 0 pontos você perde! \n\n''')
sleep(5)
pontuacao = 10
nome = int(input('Escolha um número de 0 a 5 : '))
resposta = randint(0, 5)
tentativa = 1
print('PROCESSANDO..........')
sleep(2)
while not nome == resposta:
    tentativa += 1
    if nome > resposta:
        nome = int(input('Errou! Tente um número menor!: '))
        print('Processando...')
        sleep(1)
    elif nome < resposta:
        nome = int(input('Errou! Tente um número maior!: '))
        print('Processando...')
        sleep(1)
    pontuacao -= 2
    if tentativa > 5:
        print('GAME OVER! O computador escolheu o número {}'.format(resposta))
if pontuacao >= 0:
    print('''Acertou! O computador escolheu o número {}
Você fez um total de {} pontos'''.format(resposta, pontuacao))
else:
    print('GAME OVER! O computador escolheu o número {}'.format(resposta))
