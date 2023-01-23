val = float(input('valor: '))
con = int(input("""
        0: à vista com dinheiro ou cheque
        1: à vista no cartão
        2: 2x no cartão
        3: 3x no cartão

        """))
if con < 0 or con > 3:
    print('condição de pagamento inválida')
elif con == 0:
    print(' '*7,'valor: {}'.format(val*0.9))
elif con == 1:
    print(' '*7,'valor: {}'.format(val*0.95))
elif con == 2:
    print(' '*7,'valor: {}'.format(val))
elif con == 3:
    print(' '*7,'valor: {}'.format(val*1.2))

