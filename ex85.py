lista =[[], []]
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[1].sort()
lista[0].sort()
print('=-'*30)
print(f'Você digitou a lista {lista}')
print(f'Os pares são: {lista[0]}')
print(f'Os Ímpares são: {lista[1]}')
print('=-'*30)