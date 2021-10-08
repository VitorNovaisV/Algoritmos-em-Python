maior = 0
menor = 0
for p in range (1,6):
    peso= float(input(f'Digite o peso da {p}º Pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O Maior peso lido foi de {maior:.1f}KG.')
print(f'O Menor peso lido foi de {menor:.1f}KG.')