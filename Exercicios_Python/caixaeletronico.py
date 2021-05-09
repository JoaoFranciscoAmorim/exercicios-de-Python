valor=int(input('Qual o valor que você quer sacar? R$'))
cinquenta=valor//50
cinquentaresto=valor%50
vinte=0
dez=0
um=0
if cinquentaresto != 0:
    vinte=cinquentaresto//20
    vinteresto=cinquentaresto%20
    if vinteresto != 0:
        dez = vinteresto // 10
        dezresto = vinteresto % 10
        if dezresto != 0:
            um = dezresto // 1
print('Total de {} cédulas de R$50'.format(cinquenta))
print('Total de {} cédulas de R$20'.format(vinte))
print('Total de {} cédulas de R$10'.format(dez))
print('Total de {} cédulas de R$1'.format(um))
print('Tenha um bom dia!')