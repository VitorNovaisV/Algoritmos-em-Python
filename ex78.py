lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-' * 30)
print(f'Você digitou: {lista} ')
print(f'o maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...')
print(f'o menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...')
print('=-' * 30)
