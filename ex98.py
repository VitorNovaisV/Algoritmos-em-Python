from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        print('fim')


# a
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora defina você os parametros:')
de = int(input('De: '))
ate = int(input('Até: '))
pulando = int(input('Pulando de: '))
print('=-'*30)
contador(de, ate, pulando)
