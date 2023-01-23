v=float(input('valor da casa: '))
s=float(input('salario: '))
y=int(input('quantos anos: '))
m=y*12
p=v/m
if p > 0.3*s:
    print('negado: valor excede 30% do salário')
else:
    print('cedido: valor aceitável')
 
