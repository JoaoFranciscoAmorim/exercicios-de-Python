cont=0
contm=0
contf=0
while True:
    i=int(input('Qual a idade? '))
    s=' '# para repetir caso não coloque nem f nem m. Tem que ter o espaço no meio
    while s not in 'mf':# para repetir caso não coloque nem f nem m
        s=input('Qual o sexo? [M/F] ').strip().lower()[0]
    e=' '# mesma coisa que o de cima
    while e not in 'sn':# mesma coisa que o de cima
        e=input('\033[33mQuer continuar? [S/N]: \033[m').strip().lower()[0]
    if i >= 18:
        cont = cont + 1
    if s=='m':
        contm=contm+1
    if s=='f' and i<20:
        contf=contf+1
    if e=='n':
        break
print('''\033[34m-=-DADOS DAS PESSOAS CADASTRADAS-=-
\033[35mUm total de {} pessoas possuem mais de 18 anos.
\033[mUm total de {} homens foram cadastrados.
\033[34mUm total de {} mulher(es) possui(em) menos de 20 anos.'''.format(cont,contm,contf))
print('\033[35mPrograma encerrado.')