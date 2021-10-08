matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior2linha = soma3coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}:  '))
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print('=-'*30)
print(f'A soma dos pares é {somapar}')
for linha in range(0, 3):
    soma3coluna += matriz[linha][2]
print(f'A soma da terceira coluna é {soma3coluna}')
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior2linha:
        maior2linha = matriz[1][coluna]
print(f'O maior Número da 2 linha é {maior2linha}')