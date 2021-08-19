# Analisador de triângulos v2.0
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
Triangulo = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
Equilatero = r1 == r2 and r3 == r1
Isoceles = r1 == r2 and r3 != r1 and r3 != r2 or r3 == r2 and r3 != r1 or r1 == r3 and r1 != r2
Escaleno = r1 != r2 and r3 != r1
if Triangulo and Equilatero:
    print('Podem Formar Triângulo Classificação: EQUILÁTERO')
elif Triangulo and Isoceles:
    print('Podem Formar Triângulo Classificação: ISÓCELES!')
elif Triangulo and Escaleno:
    print('Podem Formar Triângulo Classificação: ESCALENO!')
else:
    print('Não podem formar triângulo.')
