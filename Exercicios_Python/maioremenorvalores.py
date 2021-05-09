n=0
s=1
soma=0
contador=0
maior=menor=0
while s!=0:
    n=float(input('Digite um número: '))
    s=int(input('Quer continuar? ([1] para S e [0] para N): '))
    soma=soma+n
    contador=contador+1
    if n>maior:
        maior=n
    else:
        menor=n
media=soma/contador
print('A média dos {} números foi {:.2f}'.format(contador,media))
print('O menor valor foi {} e o maior foi {}'.format(menor,maior))
print('FIM')
