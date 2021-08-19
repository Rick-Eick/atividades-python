# Analisador de nomes
from time import sleep
Nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(3)
print('Seu nome em maiúsculas é {}'.format(Nome.upper()))
print('Seu nome em minúsculas é {}'.format(Nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(Nome) - Nome.count(' ')))
Separa = Nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(Separa[0], len(Separa[0])))
