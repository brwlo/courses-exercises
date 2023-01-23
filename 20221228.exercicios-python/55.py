maiornome = ''
menornome = ''
maiorpeso = 0
menorpeso = 0
for c in range(1,5):
    nome = input('nome: ')
    peso = float(input('peso: '))
    if c == 1:
        menorpeso = peso
    if peso > maiorpeso:
        maiorpeso = peso
        maiornome = nome
    elif peso == maiorpeso:
        maiornome += ", " + nome
    if peso < menorpeso:
        menorpeso = peso
        menornome = nome
    elif peso == menorpeso:
        menornome += ", " + nome
print('MAIOR:\nnome: {}\npeso: {}'.format(maiornome,maiorpeso))
print('MENOR:\nnome: {}\npeso: {}'.format(menornome,menorpeso))

