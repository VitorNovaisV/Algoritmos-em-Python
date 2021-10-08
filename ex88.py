from time import  sleep
from random import randint
temp = []
jogos = []
print('=-'*30)
print('EMULADOR DE MEGA SENA')
print('=-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
            if cont >= 6:
                break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    tot += 1
print('-=' * 3, f'Sortendo {quant} Jogos', '-='* 3)
for i, l in enumerate(jogos):
    print(f'Jogos {i+1}: {l}')
    sleep(1)
print('=-'*3, '<<<Boa Sorte Ae Amigão B)>>>', '=-'*30)
