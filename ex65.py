resposta = 'S'
soma = quantidade = media = maior = menor= 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()
    if resposta not in "NnSs":
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma / quantidade
print('=-'*30)
print(f'Você digitou {quantidade} Valores \nA soma deles é {soma} \nA média {media}\nO menor número foi {menor}\nE o maior número foi {maior}')
print('=-'*30)
