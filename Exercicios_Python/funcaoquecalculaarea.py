def area(a,b):
    s=a*b
    print('A área do terreno {} por {} é igual a {:.2f} metros quadrados.'.format(a,b,s))


larg=float(input('Largura (em metros): '))
comprimento=float(input('Comprimento (em metros): '))
area(larg,comprimento)
