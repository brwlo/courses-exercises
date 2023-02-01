sum = 0
for c in range(0,6):
    n = int(input('numero inteiro ({} de 6): '.format(c)))
    if n % 2 == 0:
        sum += n
print('soma dos números pares dentre os seis numeros: ',sum)

