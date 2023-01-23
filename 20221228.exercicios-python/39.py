from time import strftime
nas = int(input('nasc: '))
ano = int(strftime('%Y'))
ida = ano - nas
if ida < 18:
    print('ainda irás te alistar no serviço militar')
elif ida == 18:
    print('é hora de te alistares no serviço militar')
else:
    print('já passou tua hora de te alistares no serviço militar')

