# Validação de dados
Sexo = ['M', 'F', 'm', 'f']
A = str(input('informe seu sexo [M/F]: '))
while A not in Sexo:
    A = str(input('Dados inválidos. por favor informe seu sexo [M/F]: '))
print('Sexo {} registrado com sucesso'.format(A))
