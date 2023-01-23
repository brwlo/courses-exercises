n = int(input('numero [0:9999]: '))
u = n % 10
d = n % 100 // 10
c = n % 1000 // 100
m = n % 10000 // 1000
print('unidade: {}'.format(u))
print('dezena : {}'.format(d))
print('centena: {}'.format(c))
print('milhar : {}'.format(m))

