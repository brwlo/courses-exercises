print('Progressão Aritmética')
a0 = int(input('termo inicial: '))
r  = int(input('        razão: '))
c  = 1
while c < 11 :
    print('{:>2}º termo: {}'.format( c,a0+r*(c-1) ))
    c += 1

