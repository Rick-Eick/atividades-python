# Gerenciador de pagamento
produto = float(input('Qual é o preço normal do produto? R$ '))
print('FORMAS DE PAGAMENTO Digite:')
print('[1] À vista em dinheiro/cheque (10% de desconto)')
print('[2] À vista no cartão de crédito (5% de desconto)')
print('[3] Parcelado em até 12x no cartão de crédito (20% de juros a partir de 3x)')
pagamento = int(input('Digite a opção desejada: '))
if pagamento == 1:
    valor = produto - (produto * 10 / 100)
    print('O produto à vista em dinheiro/cheque, com 10% de desconto')
    print('fica de R$ {:.2f} por R$ {:.2f}!'.format(produto, valor))
elif pagamento == 2:
    valor = produto - (produto * 5 / 100)
    print('O produto à vista no cartão de crédito, com 5% de desconto')
    print('fica de R$ {:.2f} por R$ {:.2f}!'.format(produto, valor))
elif pagamento == 3:
    parcelas = int(input('Em quantas vezes deseja parcelar? Digite um número de 2 a 12: '))
    if parcelas == 1:
        valor = produto - (produto * 5 / 100)
        print('O produto à vista no cartão de crédito, com 5% de desconto')
        print('fica de R$ {:.2f} por R$ {:.2f}!'.format(produto, valor))
    elif parcelas == 2:
        valor = produto
        par = valor / parcelas
