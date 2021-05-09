from ex115.lib.interface import *
from ex115.lib.arquivo import *
arq='cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso.')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arq)
while True:
    resposta=menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Programa'])
    if resposta==1:
        lerArquivo(arq)
    elif resposta==2:
        cabeçalho('NOVO CADASTRO')
        nome=input('Nome: ')
        idade=leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta==3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida.')