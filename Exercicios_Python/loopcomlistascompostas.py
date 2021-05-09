lista=[]
dado=[]
maisdecem=[]
menosdecem=[]
cont=0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    cont=cont+1
    e=' '
    while e not in 'SN':
        e=input('Deseja cadastrar mais pessoas? [S/N]: ').strip().upper()[0]
    if e == 'N':
        break
print('\033[34mLista Cadastrada:{}\033[m'.format(lista))
for p in lista:
    if p[1]>=100:
        maisdecem.append(p[0])
    else:
        menosdecem.append(p[0])
print('Foram cadastradas {} pessoas'.format(cont))
print('Pessoas com mais de 100Kg: {}'.format(maisdecem))
print('Pessoas com menos de 100Kg: {}'.format(menosdecem))