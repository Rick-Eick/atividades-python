# Número por Extenso
A = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
N = int(input('Digite um número entre 0 e 20: '))
while N not in range(0, 20):
    N = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {A[N]}')
