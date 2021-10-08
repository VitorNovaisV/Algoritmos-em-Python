grupo = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F/O]: ')).upper()[0]
        if pessoa['sexo'] in 'MFO':
            break
        print('ERRO!, Por Favor, digite apenas M,F ou O.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!, Por favor, Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print(f'[A] Ao todo temos {len(grupo)} Pessoas cadastradas.')
media = soma / len(grupo)
print(f'[B] A média de idade é de {media:5.2f} Anos.')
print(f'[C] As Mulheres cadastradas foram', end=' ')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ,', end=' ')
print()
print(f'[D] Lista de pessoas que estão acima da média de idade: ')
for p in grupo:
    if p["idade"] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Fim')
