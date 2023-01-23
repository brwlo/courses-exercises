from calendar import isleap
y = isleap(int(input('ano: ')))
print('ano é bissexto?','sim' if y else 'não')
