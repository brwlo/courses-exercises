# colors
res='\033[m'
yel='\033[1;31;43m'
red='\033[1;41m'

a=float(input('lado a: '))
b=float(input('lado b: '))
c=float(input('lado c: '))
if a+b>c and b+c>a and a+c>b:
    print(yel,'dá triângulo',res)
else:
    print(red,'não dá triângulo',res)

