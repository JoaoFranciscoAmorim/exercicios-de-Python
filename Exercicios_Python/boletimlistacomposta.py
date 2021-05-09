ficha=[]
while True:
    nome=input('Nome: ')
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    ficha.append([nome, [nota1,nota2], media])
    resp=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc==999:
        break
    if opc<=len(ficha)-1:
        print('Notas de {} são: {}'.format(ficha[opc][0],ficha[opc][1]))
print('\033[35mFIM')