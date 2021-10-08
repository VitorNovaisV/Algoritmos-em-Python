soma = int(0)
cont = int(0)
for c in range (1,7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Você digitou {cont} valores pares, e a soma deles são: {soma}')
