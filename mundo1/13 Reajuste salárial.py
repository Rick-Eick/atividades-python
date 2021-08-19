# Reajuste salarial
V1 = float(input('Qual é o salário do funcionário R$'))
D = (V1 * 15) / 100
Vd = V1 + D
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(V1, Vd))
