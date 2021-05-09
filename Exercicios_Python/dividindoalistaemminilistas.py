lista=[]
listapares=[]
listaimpares=[]
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    e=' '
    while e not in 'SN':
        e=input('Deseja digitar outro valor? [S/N]: ').strip().upper()[0]
    if e == 'N':
        break
print('A lista digitada foi: {}'.format(lista))
for c in lista:
    if c % 2 == 0:
        listapares.append(c)
    else:
        listaimpares.append(c)
print('Os números pares foram: {}'.format(listapares))
print('Os números ímpares foram: {}'.format(listaimpares))