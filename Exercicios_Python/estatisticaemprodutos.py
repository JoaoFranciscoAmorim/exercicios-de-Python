cont=0
maisdemil=0
barato=0
pbarato=''
contador=0
while True:
    n=input('Qual o nome do produto? ').strip()
    p=float(input('Qual é o preço do(a) {}? R$'.format(n)))
    contador=contador+1
    e=' '
    while e not in 'sn':
        e=input('\033[33mQuer continuar? [s/n]: \033[m').strip().lower()[0]
    if p>=0:
        cont=cont+p
    if p>1000:
        maisdemil=maisdemil+1
    if contador==1 or p<barato:# para verificar o menor preço
        barato=p # para verificar o menor preço
        pbarato=n # para verificar o menor preço
    if e=='n':
        break
print('''\033[35m-=-Estatísticas de Compras-=-\033[m
A soma total dos valores dos produtos é de R${:.2f}
{} produtos custam mais de R$1000.00
O produto mais barato é o(a) {}, que custa R${:.2f}'''.format(cont,maisdemil,pbarato,barato))
print('\033[35m-=-Volte sempre!-=-')