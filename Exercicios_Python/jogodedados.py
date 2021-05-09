import random
import operator
d1=random.randint(1,6)
d2=random.randint(1,6)
d3=random.randint(1,6)
d4=random.randint(1,6)
dicionario={'J1': d1,'J2': d2,'J3': d3,'J4': d4}
rank={}
for k, v in dicionario.items():
    print('O jogador {} tirou {}'.format(k,v))
rank=sorted(dicionario.items(),key=operator.itemgetter(1),reverse=-1)
print(rank)
for i, v in enumerate(rank):
    print('{} lugar: {} com {}'.format(i+1,v[0],v[1]))

