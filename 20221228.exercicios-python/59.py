opt = 0
while 0 <= opt < 6:
    if opt == 0:
        print('forneça dois números: ')
        n1 = int(input('n1 = '))
        n2 = int(input('n2 = '))
        print('selecione uma opção:')
        print('1) somar')
        print('2) multiplicar')
        print('3) maior')
        print('4) novos números')
        print('5) sair')
        opt = int(input())
    elif opt == 1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
        opt = 0
    elif opt == 2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
        opt = 0
    elif opt == 3:
        print('greater of {} and {}: {}'.format(n1,n2,max(n1,n2)))
        opt = 0
    elif opt == 4:
        print('reescolher números:')
        opt = 0
    elif opt == 5:
        break

