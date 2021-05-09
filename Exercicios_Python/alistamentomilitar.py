import datetime
ano=int(input('Digite o seu ano de nascimento: '))
atual=datetime.date.today().year
dezoito=ano+18
if dezoito==atual:
    print('''Você nasceu em {} e faz 18 anos de idade no ano atual.
Você deve se alistar imediatamente.'''.format(ano))
elif dezoito<atual:
    maior=atual-dezoito
    print('Você tem {} anos de idade e deveria ter se alistado {} anos atrás, em {}.'.format((atual-ano),maior,dezoito))
else:
    menor=dezoito-atual
    print('Você tem {} anos de idade e ainda faltam {} anos para se alistar, em {}.'.format((atual-ano),menor,dezoito))
