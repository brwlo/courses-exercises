nome = input('nome completo: ')
print(nome.upper())
print(nome.lower())

letras = len(nome) - nome.count(' ')
print('nome: {} letras'.format(letras))

words = nome.split()
print('primeiro nome: {} letras'.format(len(words[0])))

