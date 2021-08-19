# Aquele clássico de média
Nota1 = float(input('Digite a primeira nota: '))
Nota2 = float(input('Digite a segunda nota: '))
Nota3 = float(input('Digite a terceira nota: '))
Media = (Nota1 + Nota2 + Nota3) / 3
if Media > 6:
    print('O aluno tem média igual a {:.1f}'.format(Media))
    print('APROVADO')
else:
    print('O aluno tem média igual a {:.1f}'.format(Media))
    print('REPROVADO')
