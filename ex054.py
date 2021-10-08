from datetime import date
maior = 0
menor = 0
for i in range (1,8):
    a =int(input(f'Ano de nascimento N°{i}: '))
    if date.today().year - a <18:
        menor =+1
    else:
        maior +=1
print(f'O total de Maiores de idade foi {maior}')
print(f'O total de Menores de idade foi {menor}')