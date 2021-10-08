pt = int(input('1° termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} >', end='')
    termo += r
    cont += 1
print('Fim')