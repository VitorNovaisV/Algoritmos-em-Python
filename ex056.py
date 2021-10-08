somaidade = 0
mediaidade = 0
maioridm = 0
nomevelho = 0
totmulher20 = 0
for p in range (1, 5):
    print(f'----- {p}ª Pessoa -----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridm = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridm:
        maioridm = idade
        nomevelho = nome
    if sexo in 'ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade /4
print(f'A Média de idade do grupo é de {mediaidade} anos.')
print(f'O Homem maus velho tem {maioridm} Anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} Mulheres com menos de 20 anos.')
