import math
ang = float(input('angulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('ang: {} => '.format(ang))
print('cos: {:.2f}\nsen: {:.2f}\ntan: {:.2f}'.format(cos,sen,tan))

