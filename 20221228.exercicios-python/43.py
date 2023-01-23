peso = float(input('peso: '))
altu = float(input('altura: '))
imc = peso / altu**2
if imc < 18.5:
    print('magro demais')
elif imc <= 25:
    print('peso bom')
elif imc <= 30:
    print('sobrepeso')
elif imc <= 40:
    print('obeso')
else:
    print('mórbido')

