while True:
    print('-=-' * 6)
    n=float(input('Digite um valor (negativo para sair do programa): '))
    if n<0:
        break
    print('-=-'*6)
    for c in range(1,11):
        print('\033[35m{:.0f} x {} = {:.0f}\033[m'.format(n,c,n*c))
print('\033[33mPrograma encerrado. Volte sempre!')
