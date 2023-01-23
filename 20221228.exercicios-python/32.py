a = int(input('nº a: '))
b = int(input('nº b: '))
c = int(input('nº c: '))
v = [a,b,c]
v.sort()
p = v[0]
u = v[len(v)-1]
print('menor: ',p)
print('maior: ',u)

