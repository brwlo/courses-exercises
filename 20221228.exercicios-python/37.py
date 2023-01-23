n = int(input('num. => '))
b = int(input('base => '))
if b == 2:
    print(bin(n)[2:])
elif b == 8:
    print(oct(n)[2:])
elif b == 16:
    print(hex(n)[2:])
else:
    print('base não aceitável')

