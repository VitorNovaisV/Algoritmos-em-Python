import random
print('Sou seu Computador, \n Acabei de pensar em um número entre 0 e 10 \n será que você Consegue adivinhar qual foi?')
pc = random.randint(1,10)
num = int(input('Qual o seu palpite?: '))
tentativas = 1
while num != pc:
    if num < pc:
        print('Mais..., Tente Novamente:')
        num = int(input('Qual o seu palpite?: '))
        tentativas +=1
    if num > pc:
        print('Menos..., Tente Novamente:')
        num = int(input('Qual o seu palpite?: '))
        tentativas +=1
print(f'Você Acertou em {tentativas} Tentativas. Parabéns! ')