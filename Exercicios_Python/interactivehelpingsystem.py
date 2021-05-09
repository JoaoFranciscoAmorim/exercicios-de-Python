def ajuda(com):
    titulo(f'Acessando o manual do comando {com}')
    help(com)

def titulo(msg, cor=0):
    tam=len(msg)+4
    print('~~' * tam)
    print(f'  {msg}')
    print('~~' * tam)
comando=''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando=input('Função ou Biblioteca: ').strip()
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!')