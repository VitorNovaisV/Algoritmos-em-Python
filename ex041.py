i = int(input('Digite a Idade do Atleta: '))
if i <= 9:
    c =('MIRIM')
elif i >9 and i <=14:
    c = ('INFANTIL')
elif i >14 and i <=19:
    c = ('JÚNIOR')
elif i >19 and i <=25:
    c = ('SÊNIOR')
elif i >25:
    c = ('MASTER')
print(f'A Categoria do Atleta é: {c}')
