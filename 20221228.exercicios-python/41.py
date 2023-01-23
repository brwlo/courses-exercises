from time import strftime
nas = int(input('nasc: '))
ano = int(strftime('%Y'))
ida = ano - nas
if ida < 10:
    print('mirim')
elif ida < 15:
    print('infantil')
elif ida < 20:
    print('junior')
elif ida < 26:
    print('senior')
else:
    print('master')

