lista = []
r = 's'
while r not in 'n':
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso!')
    elif n in lista:
        print('Esse número já foi digitado!')
    r = input('Você quer continuar? [S/N]: ').strip().lower()
    while r not in 'sn':
        r = input('Você quer continuar? [S/N]: ').strip().lower()
lista.sort()
print('=-'*30)
print(f'Você criou a lista com os seguintes Números:\n {lista}')
print('=-'*30)