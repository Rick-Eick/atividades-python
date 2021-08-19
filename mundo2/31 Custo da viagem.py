# Custo da Viagem
Distancia = float(input('Qual a distância da sua viagem? '))
print('Você estar preste a começar um viagem de {}km'.format(Distancia))
Preco = Distancia * 0.50 if Distancia <= 200 else Distancia * 0.45
print('O preço da sua passagem será de R${}'.format(Preco))
