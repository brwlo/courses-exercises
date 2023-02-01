n = int(input('n = '))
copy = n
f = 1
while n > 1:
    f *= n
    n -= 1
print('fatorial de {}: {}'.format(copy,f))

