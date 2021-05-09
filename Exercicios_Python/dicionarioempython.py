aluno={}
aluno['nome']=input('Nome do aluno: ')
aluno['media']=float(input('Média do aluno: '))
if aluno['media']>=6:
    aluno['situação']='Aprovado'
elif 5<=aluno['media']<=6:
    aluno['situação']='Recuperação'
else:
    aluno['situação']='Reprovado'
for k, v in aluno.items():
    print('{} é igual a {}'.format(k,v))