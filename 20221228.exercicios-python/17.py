from math import sqrt
a = float(input('cateto oposto: '))
b = float(input('cateto adjacente: '))
c = sqrt(a**2 + b**2)
print('hipotenusa: {:.2f}'.format(c))

# or:
# from math import hypot
# c = hypot(a,b)
# print(c)
