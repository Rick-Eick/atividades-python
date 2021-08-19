# Detector de palíndromo
Frase = input('Qual a frase? ').upper().replace(' ', '')
if Frase == Frase[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
