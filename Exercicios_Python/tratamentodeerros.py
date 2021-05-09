def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n
n1=leiaint('Digite um valor inteiro: ')
n2=leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1}')
print(f'O valor real digitado foi {n2}')