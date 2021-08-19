# Aprovando empréstimo
Casa = float(input('Valor da Casa: R$'))
Salario = float(input('Salário do comprador: R$'))
Anos = int(input('Em quantos anos deseja pagar: '))
Prestacao = Casa / (Anos * 12)
Minimo = (Salario * 30) / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(Casa, Anos))
print('a prestação será de R${:.2f}'.format(Prestacao))
if Prestacao <= Minimo:
    print("Empréstimo CONCEDIDO")
else:
    print('Empréstimo NEGADO')
