n = (int(input('Digite um número: ')),
     int(input('Digite Outro número: ')),
     int(input('Digite Mais um número: ')),
     int(input('Digite o Último número: ')))
print(f'Você digitou os valores {n}')
print(f'o valor "9" apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro valor 3 apareceu na posição {n.index(3)+1}')
else:
    print('O Valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados foram: ')
for a in n:
    if a % 2 == 0:
        print(a, end=" ")
