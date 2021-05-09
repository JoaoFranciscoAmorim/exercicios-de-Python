import random
while True:
    n=int(input('Faça sua jogada: '))
    p=input('Quer par ou ímpar? [P/I]').strip().lower()[0]
    comp=random.randint(1,10)
    if (n+comp)%2==0 and p=='p':
        print('O PC escolheu {} e você {}, a soma deu {}, que é par. Você ganhou!'.format(comp,n,n+comp))
    elif (n+comp)%2!=0 and p=='i':
        print('O PC escolheu {} e você {}, a soma deu {}, que é ímpar. Você ganhou!'.format(comp,n,n+comp))
    else:
        print('O PC escolheu {} e você {}, a soma deu {}. Você perdeu!'.format(comp, n, n + comp))
        break
print('\033[33mFIM DE JOGO')