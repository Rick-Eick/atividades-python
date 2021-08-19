# Aluguel de carros
D = int(input('Quantos dias o carro foi alugado? '))
P = float(input('Quantos Km foi pecorrido? '))
T = (D*60)+(P*0.15)
print('O total a pagar é R${:.2f}'.format(T))
