lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    r = input('Quer continuar? [S/N]: ').strip().lower()
    while r not in 'sn':
        r = input('Quer continuar? [S/N]: ').strip().lower()
    if r == 'n':
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} Números em sua lista')
print(f'Os Valores em ordem decrecente são: {lista}')
if 5 in lista:
    print('O valor "5" esta na lista')
else:
    print('O valor "5" não esta na lista.')