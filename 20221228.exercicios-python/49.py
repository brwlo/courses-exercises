m = int(input('Diga uma número: '))
print('Taboada do {}'.format(m))
print(18*'-')
for c in range(0,11):
    print('  {:>2} × {} = {:>2}'.format(c,m,c*m))
print(18*'-')

