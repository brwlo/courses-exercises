print('Progressão Aritmética')
a0 = int(input('termo inicial: '))
r  = int(input('        razão: '))
for c in range(1,11):
    print('{:^2}º termo: {}'.format( c,a0+r*(c-1) ))

