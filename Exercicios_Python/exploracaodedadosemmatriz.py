matriz=[[0,0,0], [0,0,0], [0,0,0]]
spar=mai=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input('Digite um valor para a posição [{}, {}]: '.format(l,c)))
print('-=-'*12)
for l in range(0,3):
    for c in range(0,3):
        print('[{:^5}]'.format(matriz[l][c]),end='')
        if matriz[l][c]%2==0:
            spar=spar+matriz[l][c]
    print()
print('-=-'*12)
print('A soma dos valores pares é {}'.format(spar))
for l in range(0,3):
    scol=scol+matriz[l][2]
print('A soma dos valores da terceira coluna é {}'.format(scol))
for c in range(0,3):
    if c==0:
        mai=matriz[1][c]
    elif matriz[1][c] > mai:
        mai=matriz[1][c]
print('O maior valor da segunda linha é {}'.format(mai))