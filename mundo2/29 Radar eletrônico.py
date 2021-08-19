# Radar eletrônico
A = int(input('Qual a velocidade atual do carro? '))
if A < 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    Multa = (A - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(Multa))
    print('Tenha um bom dia! Dirija com segurança')
