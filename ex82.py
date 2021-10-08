lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    r = input('Quer Continuar? [S/N]: ').strip().lower()
    while r not in 'sn':
        r = input('Quer Continuar? [S/N]: ').strip().lower()
    if r in 'n':
        break
lista.sort()
pares.sort()
impares.sort()
print(f'Você criou a lista com os números {lista}')
print(f'Uma lista apenas com valores pares é {pares}')
print(f'Uma lista apenas com valores Ímpares é {impares}')