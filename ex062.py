pt = int(input('1° termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
numari = 10
while numari != 0:
    while cont <= numari:
        print(f'{termo} >', end='')
        termo += r
        cont += 1
    print('Fim')
    numari = int(input('\nQuantos termos você quer mostrar a mais?: '))
    cont = 1
print('Programa Finalizado.')