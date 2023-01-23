n = int(input('nº: '))
primo = 'yes'
for c in range(2,n):
    if (n % c == 0):
        primo = 'no'
print('primo? ',primo)

