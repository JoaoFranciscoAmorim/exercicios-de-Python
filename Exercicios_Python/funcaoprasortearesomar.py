import random
def sorteia(lista):
    for cont in range(0,5):
        n=random.randint(1,10)
        lista.append(n)
        print(f'{n} ',end='', flush=True)
    print('PRONTO')

def somapar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros=[]
sorteia(numeros)
somapar(numeros)