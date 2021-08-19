# Primeiro e última nome de uma pessoa
N = str(input('Digite seu nome completo: ')).strip()
Nome = N.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(Nome[0]))
print('Seu último nome é {}'.format(Nome[len(Nome)-1]))
