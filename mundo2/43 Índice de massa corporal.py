# Índice de massa corporal
Peso = float(input('Digite seu peso Kg: '))
Altura = float(input('Digite sua altura m: '))
Imc = Peso / (Altura ** 2)
print('Você está com uma massa corporal de {:.1f}'.format(Imc))
if Imc < 18.5:
    print('Você está ABAIXO da média de peso.')
elif Imc <= 25:
    print('Você está no peso IDEAL')
elif Imc < 30:
    print('Você está com um nível de SOBREPESO.')
elif Imc <= 40:
    print('Você está com um nível de OBESIDADE.')
else:
    print('Você está com um nível de OBESIDADE MÓRBIDA.')
