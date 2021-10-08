time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome Do Jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} Jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos Gols {jogador["nome"]} fez na {c+1}º Partida?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!, Digite apenas [S] ou [N]')
    if resp == 'N':
        break
print('=-'*30)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' ---- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     no jogo {i+1} fez {g} gols.')
    print('-'*40)
print('fim')


