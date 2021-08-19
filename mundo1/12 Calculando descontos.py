# Calculando descontos
V1 = float(input('Qual o preço do produto? R$'))
D = (V1 * 5) / 100
Vd = V1 - D
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(V1, Vd))
