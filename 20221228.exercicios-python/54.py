from time import strftime
agora = int(strftime('%Y'))
maiores = 'maiores de idade: \n'
for c in range(0,7):
    nome = input('nome: ')
    ano  = int(input('ano nasc. pessoa {}: '.format(c)))
    if agora - ano > 22:
        maiores += nome + '\n'
print(maiores)

