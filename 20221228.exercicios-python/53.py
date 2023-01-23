frase = input('frase: ').replace(' ','')
rever = ''
for i in range(len(frase)-1,-1,-1):
    rever += frase[i]
if frase == rever:
    print('palindromo')
else:
    print('não palindromo')

