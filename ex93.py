jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome Do Jogador: ')).strip().capitalize()
tot = int(input(f'Quantas partidas {jogador["nome"]} Jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos Gols {jogador["nome"]} fez na {c+1}º Partida?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
for k, v in jogador.items():
    print(f'O Campo {k} tem o valor {v}')
print('=-'*30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f' ---- Na Partida {i+1}, fez {v} Gols')
print(f'Foi um total de {jogador["total"]} Gols ')