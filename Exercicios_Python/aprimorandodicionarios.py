jogador={}
partidas=[]
time=[]
while True:
    jogador.clear()
    jogador['nome']=input('Nome do jogador: ')
    tot=int(input('Quantas partidas {} jogou? '.format(jogador["nome"])))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=input('Quer continuar? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp=='N':
        break
print('-='*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca=int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca==999:
        break
    if busca>=len(time):
        print('ERRO! Não existe jogador com código {}!'.format(busca))
    else:
        print('\033[34m-=-LEVANTAMENTO DO JOGADOR {}-=-\033[m'.format(time[busca]["nome"]))
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*35)
print('\033[33mFIM\033[m')