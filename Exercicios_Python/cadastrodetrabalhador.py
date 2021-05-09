import datetime
dados={}
dados['nome']=input('Nome: ')
nasc=int(input('Ano de nascimento: '))
dados['idade']=datetime.datetime.now().year - nasc
dados['ctps']=int(input('Carteira de Trabalho [0 não tem]: '))
if dados['ctps']!=0:
    dados['contratação']=int(input('Ano de Contratação: '))
    dados['salario']=float(input('Salário: R$'))
    dados['aposentadoria']=dados['idade']+((dados['contratação']+35)-datetime.datetime.now().year)
for k, v in dados.items():
    print('- {} tem o valor {}'.format(k,v))