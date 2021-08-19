# Aumentos multiplos
Salario = float(input('Qual o salário do funcionário? R$'))
Porcetagem = 0
SalarioN = 0
if Salario > 1250:
    Porcetagem = (Salario * 10) / 100
    SalarioN = Salario + Porcetagem
else:
    Porcetagem = (Salario * 15) / 100
    SalarioN = Salario + Porcetagem
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(Salario, SalarioN))
