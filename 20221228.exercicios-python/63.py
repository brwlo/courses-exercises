n = int(input('n = '))
f1 = 0
f2 = 1
f = 0
c = 2
print(f1)
print(f2)
while c <= n:
    f = f1 + f2
    print(f)
    f1 = f2
    f2 = f
    c += 1

