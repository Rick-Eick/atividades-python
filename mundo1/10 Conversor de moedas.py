# Conversor de moedas
N = float(input('Quanto dinheiro você tem na carteira? '))
D = N / 3.27
print('Com R${} você pode comprar US${:.2f}'.format(N, D))
