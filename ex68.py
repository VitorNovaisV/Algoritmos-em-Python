from random import randint
vit = 0
print('=-'*30)
print('Vamos Jogar Par ou Ímpar!')
print('=-'*30)
while True:
    num = int(input('Digite Um Número: '))
    res = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    comp = randint(0, 10)
    total = num + comp
    while res not in 'PI':
        res = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    print('=-'*30)
    print(f'Você Jogou {num} e o Computador {comp}. Total de {total}')
    if res == 'P':
        if total % 2 == 0:
            vit =+1
            print('Deu Par.\nVocê Ganhou! Vamos Jogar Denovo.')
            print('=-'*30)
        else:
            print('Deu Ímpar.\nVocê Perdeu.')
            print('=-' * 30)
            break
    if res == 'I':
        if total % 2 == 1:
            vit =+1
            print('Deu Ímpar.\nVocê Ganhou! Vamos Jogar Denovo.')
            print('=-'*30)
        else:
            print('Deu Par.\nVocê Perdeu.')
            print('=-' * 30)
            break
print('Fim De Jogo!')
print(f'Você Ganhou {vit} Vezes!')
print('=-'*30)