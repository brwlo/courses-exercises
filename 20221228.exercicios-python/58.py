from random import randint
n = randint(1,5)
count = 0
guess = int(input('adivinhe: '))
while guess != n:
    count += 1
    print('errado. tente de novo.')
    guess = int(input('adivinhe: '))
print(' erros: ',count)
print('numero: ', guess)

