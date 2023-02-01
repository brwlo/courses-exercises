print('Progressão Aritmética')
a0 = int(input('termo inicial: '))
r  = int(input('        razão: '))
an = a0
c  = 0
lim = 10
while c < lim:
    print(an)
    an = an+r
    c += 1
    if c == 10:
        x = int(input('quantos mais termos? '))
        lim = 10 + x
