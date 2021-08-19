# procurando uma string dentro da outra
Nome = str(input('Qual seu nome completo? '))
print('Seu nome tem Silva?', end=' ')
print(Nome.find('Silva') > 0)
