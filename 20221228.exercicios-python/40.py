n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
md = (n1 + n2) / 2
print(md)
if md < 5:
    print('reprovado')
elif 5 <= md < 7:
    print('recuperado')
else:
    print('aprovado')

