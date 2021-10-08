#027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome: ')).strip()
x = nome.split()
print (f'Seu nome é {nome.title()}')
print(f' o seu primeiro nome é:{x[0]}')
print(f' o seu último nome é: {x[-1]}')











