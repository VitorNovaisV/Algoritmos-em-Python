from random import randint
itens = ('nada','Pedra', 'Papel', 'Tesoura')
pc = randint(1, 3)
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jog = int(input('Qual a Sua jogada?:'))
print('=-' * 10)
print(f'O Computador Jogou: {(itens[pc])}')
print(f'Você Jogou: {(itens[jog])}')
print('=-' * 10)
if pc == 1: #pedra
    if jog == 1:
        print('Empate!')
    elif jog == 2:
        print('Você Ganhou!')
    elif jog == 3:
        print('Você Perdeu!')
    else:
        print('Jogada Invalida')
elif pc == 2: #papel
    if jog == 1:
        print('Você Perdeu')
    elif jog == 2:
        print('Empate!')
    elif jog == 3:
        print('Você Ganhou!')
    else:
        print('Jogada Invalida')
elif pc == 3: #tesoura
    if jog == 1:
        print('Você Ganhou!')
    elif jog == 2:
        print('Você Perdeu!')
    elif jog == 3:
        print('Empate!')
    else:
        print('Jogada Invalida')





