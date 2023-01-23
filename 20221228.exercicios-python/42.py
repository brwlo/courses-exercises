a=float(input('lado a: '))
b=float(input('lado b: '))
c=float(input('lado c: '))

if a+b>c and b+c>a and a+c>b:
    if a == b == c:
        print('equilátero')
    elif (a == b and a != c) or (a == c and a != b):
        print('isóceles')
    else:
        print('escaleno')
else:
    print('não é triangulo')

