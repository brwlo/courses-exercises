from random import randrange
choices = {0:'pedra',1:'papel',2:'tesoura'}
comp = randrange(3)
user = int(input('0: pedra; 1: papel; 2: tesoura ')) % 3
print('você escolheu: ',choices[user])
print('ele  escolheu: ',choices[comp])
print('você ',end='')
if user == comp:
    print('empatou')
elif user < comp:
    if comp - user == 1:
        print('perdeu')
    else:
        print('ganhou')
elif user > comp:
    if user - comp == 1:
        print('ganhou')
    else:
        print('perdeu')

