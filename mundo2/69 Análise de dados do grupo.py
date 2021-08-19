# Análise de dados do grupo
dezoito = masculino = vinte = 0
while True:
    idade = int(input('qual sua  idade ?'))
    sexo = str(input('digite seu sexo F/M')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('digite seu sexo F/M')).strip().upper()[0]
    conti = str(input('deseja parar? digite N se não S ')).strip().upper()[0]
    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        if idade >= 20:
            vinte += 1
    if conti == 'N':
        break
print(f'tem {dezoito} pessoas maior de 18')
print(f'tem {masculino} pessoas do sexo masculino')
print(f'tem {vinte} mulheres acima de 20 anos ')
