import random
lista=[]
jogos=[]
quant=int(input('Quantos jogos você quer jogar? '))
tot=1
while tot<=quant:
    cont=0
    while True:
        num=random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont=cont+1
        if cont>=6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot=tot+1
for i, l in enumerate(jogos):
    print('JOGO {}: {}'.format(i+1,l))