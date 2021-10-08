from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
rank = sorted(dados.items(), key=itemgetter(1),reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)