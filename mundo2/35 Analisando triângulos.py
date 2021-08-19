# Analisando triângulos
print('=-=-=-=-=-=-=-=-=-=-=-=-=')
print('ANALISADOR DE TRIÂNGULOS')
print('=-=-=-=-=-=-=-=-=-=-=-=-=')
A = float(input('Primeiro segmento: '))
B = float(input('Segundo segmento: '))
C = float(input('Terceiro segmento: '))
if A + B >= C:
    print('Estes segementos PODEM CRIAR um triângulo!')
else:
    print('Estes segementos NÃO PODEM CRIAR um triângulo!')
