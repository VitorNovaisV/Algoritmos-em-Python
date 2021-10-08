import random
print(f'{" ""="*27} \n Vou Pensar em Um Número entre 0 e 5, Tente Adivinhar!\n{" ""="*27}')
num = random.randint(0,5)
jg = int(input('Qaul Número você acha q foi?: '))
if jg == num:
    print('Parabéns!! Você Acertou!!')
else:
    print('Desculpe,Não foi dessa vez :/')