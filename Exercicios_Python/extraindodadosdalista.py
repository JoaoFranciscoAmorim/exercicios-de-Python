lista=[]
cont=0
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    cont=cont+1
    e=' '
    while e not in 'SN':
        e=input('Deseja digitar outro valor? [S/N]: ').strip().upper()[0]
    if e == 'N':
        break
print('A lista digitada foi: {}'.format(lista))
lista.sort(reverse=-1)
print('A lista possui {} valores'.format(cont))
print('A lista,em ordem decrescente, é: {}'.format(lista))
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')