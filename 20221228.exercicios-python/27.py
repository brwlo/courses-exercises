from random import randint
n = randint(1,5)
if (int(input('adivinhe: ')) == n):
    print('certo! é {}.'.format(n))
else:
    print('errado. era {}.'.format(n))

