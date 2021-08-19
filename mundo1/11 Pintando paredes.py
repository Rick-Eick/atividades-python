# Pintando Parede
L = float(input('Largura da parede: '))
A = float(input('Altura da parede:'))
Area = L * A
T = Area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}'.format(L, A, Area))
print('Para pintar essa parede, você presisará de {}l de tintas'.format(T))
