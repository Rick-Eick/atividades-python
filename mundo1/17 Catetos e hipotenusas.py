# Catetos e hipotenusas
Co = float(input('comprimento do cateto oposto: '))
Ca = float(input('comprimento do cateto adjacente: '))
Hi = (Co**2 + Ca**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(Hi))
