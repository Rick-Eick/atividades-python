# Seno, cosseno e tangente
import math
Angulo = float(input('Digite o valor do ângulo: '))
Seno = math.sin(math.radians(Angulo))
Cosseno = math.cos(math.radians(Angulo))
Tangente = math.tan(math.radians(Angulo))
print('O ângulo de {} tem seno de {:.2f}'.format(Angulo, Seno))
print('O ângulo de {} tem cosseno de {:.2f}'.format(Angulo, Cosseno))
print('O ângulo de {} tem tangente de {:.2f}'.format(Angulo, Tangente))
