algo = input('Digite algo: ')
print('O tipo primitivo é: ',type(algo))
print('Só tem espaços: ',algo.isspace())
print('É número: ',algo.isnumeric())
print('É alfabético: ',algo.isalpha())
print('É alfanumérico: ',algo.isalnum())
print('É maiúsculo: ',algo.isupper())
print('Está capitalizado: ',algo[0].isupper())

