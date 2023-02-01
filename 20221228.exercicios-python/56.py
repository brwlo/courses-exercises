nome = ''
sexo = ''
idade = 0
maior = 0
media = 0
velho = ''
men20 = 0
for c in range(1,5):
    nome  = input('nome: ')
    sexo  = input('sexo (m/f): ')
    idade = int(input('idade: '))
    media += idade
    if sexo == 'm' and idade > maior:
        maior = idade
        velho = nome
    if sexo == 'f' and idade < 20:
        men20 += 1
print('\n')
print(' MÉDIA DE IDADE: ',media/4)
print('     MAIS VELHO: ',velho)
print('NOVINHAS (<20a): ',men20)

