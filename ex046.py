from time import sleep
print('Acender fogos? \n [1] sim \n [2] Não')
e = int(input('Escolha: '))
if e == 1:
    for a in range(10,0,-1):
        sleep(1)
        print(a)
    print('*Explosão')
    sleep(6)
    print('os Fogos na realidade eram bombas atômicas')
    sleep(3)
    print('a raça humana foi extinta')
    sleep(6)
    print('O mundo está em cinzas')
    sleep(5)
    print('Dos poucos objetos que restaram da civilização apenas um está inteiro')
    sleep(1.5)
    print('Sem nenhum arranhão')
    sleep(6)
    print('Um Nokia Tijolão')
elif e == 2:
    print('Ok')
else:
    print('Não, digita 1 ou 2, animal')